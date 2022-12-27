# HPDS Server
Get System information through API

## Installation
1. Install Python 3.10
2. Create a virtual environment
   ```bash
    python -m venv .venv
    ```
3. Activate the virtual environment
   ```bash
    source .venv/bin/activate
    ```
4. Install poetry
   ```bash
    pip install poetry
    ```
5. Install dependencies
   ```bash
    poetry install
    ```
6. Create a MYSQL database with the name `hpds`
   ```bash
    mysql -u root -p
    CREATE DATABASE hpds;
    ```
7. Install the database
   ```bash
   alembic upgrade head
   ```
8. Run the server
   ```bash
   uvicorn app.main:app --reload
    ```

## API Documentation
The API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs)

## For each system you need to install agent
   agent is available at [https://github.com/mortezasaki/hpds_agent](https://github.com/mortezasaki/hpds_agent)