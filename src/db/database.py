import psycopg2
from psycopg2.extensions import connection

from .config import load_db_config


def get_connection(dbname: str = "northwind") -> connection:
    """Создаёт и возвращает подключение к указанной базе PostgreSQL."""
    params = load_db_config(dbname)

    conn = psycopg2.connect(**params)  # pyright: ignore[reportCallIssue, reportArgumentType]

    return conn
