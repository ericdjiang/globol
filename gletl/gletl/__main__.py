from gldb.mongo import MongoClient
from gldb.postgres import PostgresSession

def app():
    with MongoClient() as client:
        db = client.web
        print("Mongo DB handle:\n", db)


def pgapp():
    with PostgresSession() as session:
        print("Postgres DB session:\n", session)


if __name__ == "__main__":
    app()
    pgapp()
