from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.infrastructure.config.settings import get_settings
from contextlib import contextmanager

settings = get_settings()

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine)

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise 
    finally:
        db.close()