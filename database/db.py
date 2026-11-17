from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.config import DB


engine = create_engine(DB.DATABASE_URL)


SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)