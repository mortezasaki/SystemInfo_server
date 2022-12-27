FROM python:3.10-slim-buster as requirements-stage

WORKDIR /tmp 
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10-slim-buster
RUN apt-get update && apt-get install gcc -y && apt-get clean
WORKDIR /hpds_server
COPY --from=requirements-stage /tmp/requirements.txt /hpds_server/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /hpds_server/requirements.txt
COPY ./src /hpds_server
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]

