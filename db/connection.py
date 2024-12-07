import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables from the .env file
load_dotenv()

# Define the base class for declarative models
Base = declarative_base()


def connect_to_mysql():
    """
    method used to connect mysql database
    :return: session, engine
    """
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    port = os.getenv("DB_PORT", 3306)  # Default to 3306 if not set

    # Construct the MySQL database URL for SQLAlchemy
    DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db_name}"

    # Create an engine to connect to MySQL
    engine = create_engine(DATABASE_URL, echo=True)

    # Create a session maker bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session to interact with the database
    session = Session()

    return session, engine


