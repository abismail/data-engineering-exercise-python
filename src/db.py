import sqlite3


def upsert_new():
    with sqlite3.connect("warehouse.db") as con:
        cursor = con.cursor()
