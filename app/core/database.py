from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#defining our URL to the database (shouldb be stored at .env file)
SQLALCHEMY_DATABASE_URL = 'postgresql://user:password@localhost:5432/postgres'

#creating the core of the database instance this way
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#a session is used to connect to the database to make changes to it 
SessionLocal = sessionmaker(autocommit=False , autoflush=False , bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()  # creating a session stored at db
    try: # to catch erros
        yield db # create the db
    finally:
        db.close
