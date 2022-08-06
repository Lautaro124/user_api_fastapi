# Simple users API

## Requirements install
pip install fastapi fastapi-sqlalchemy pydantic alembic psycopg2 uvicorn python-dotenv

## Docker up container
you can use:

docker-compose build
docker-compose up

or:

docker-compose up -d --build


## Migrate with alembic
docker-compose run app alembic revision --autogenerate -m "New Migration"
docker-compose run app alembic upgrade head
