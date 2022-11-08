import json
import sys
import polars


def drop_inliers(votes):
    mean = votes.mean()
    std_dev = votes.std()
    inliers = (votes - mean).abs() <= (2 * std_dev)
    return inliers


try:
    pl_votes = polars.read_ndjson(sys.argv[1])
    print("OG data")
    print(pl_votes)
    print("===========================================================================")

    pl_votes_by_creation_date = pl_votes.sort("CreationDate")
    pl_votes_by_week = pl_votes_by_creation_date.groupby_dynamic(
        "CreationDate", every="1w"
    ).agg(polars.col("VoteTypeId").mean())
    pl_votes_weekly_avg = pl_votes_by_week
    print("data to be removed")
    print(pl_votes_weekly_avg)

    pl_votes_with_week = pl_votes.withColumn(
        polars.col("CreationDate").dt.week().alias("week")
    )
except FileNotFoundError:
    print("Please download the dataset using 'make fetch_data'")
