from pony.orm import Database

from app.core.config import settings

RDBMS="postgres"

def connect_db() -> Database:
    db = Database()
    db.bind(
        provider=RDBMS,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        host=settings.POSTGRES_SERVER,
        database=settings.POSTGRES_DB,
        options=settings.POSTGRES_OPTIONS
    )
    return db

db = connect_db()
