import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv("../.env")

engine = create_engine(
    "postgresql://{}:{}@localhost:{}/{}".format(
        os.environ["POSTGRES_USER"],
        os.environ["POSTGRES_PASSWORD"],
        os.environ["POSTGRES_PORT"],
        os.environ["POSTGRES_DB"],
    )
)

PostgresSession = sessionmaker(engine)
