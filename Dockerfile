FROM python:3.10.4-slim as base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

FROM base AS python-deps

RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev curl sqlite3
RUN apt-get autoremove -y
RUN pip install pipenv==2022.11.5
RUN pip install mypy
RUN pip install flake8
RUN pip install polars

WORKDIR /root/

COPY src /root/src/
COPY scripts /root/scripts/
COPY setup.cfg Makefile Pipfile Pipfile.lock /root/

COPY uncommitted /root/uncommitted/
# COPY  /root/Makefile
# COPY  /root/Pipfile
# COPY /root/setup.cfg
# COPY setup.py /root/setup.py

RUN chmod -R +x scripts/*.sh

RUN pipenv install --system --deploy
# \
# --dev \
#  && pipenv lock -r > requirements.txt \

# RUN make fetch-data
# RUN python src/main.py
