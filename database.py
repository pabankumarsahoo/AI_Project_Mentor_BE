import urllib.parse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

server = r"HP\SQLEXPRESS"
database = "AIProjectMentor"

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

params = urllib.parse.quote_plus(connection_string)

DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()