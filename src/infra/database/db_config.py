from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = os.environ.get('RELATIONAL_DB_URI')

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def create_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as ex:
        raise Exception("Error in configure database - {}".format(str(ex)))


def init_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def close_session(session):
    session.close()
