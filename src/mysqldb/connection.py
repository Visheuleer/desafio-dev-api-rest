from core import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DataBaseConnection:
    def __init__(self):
        self.engine = create_engine(f"mysql+mysqlconnector://{settings.get_db_user()}:{settings.get_db_password()}@{settings.get_db_host()}:{settings.get_db_port()}/{settings.get_db_name()}")
        self.db_session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)


db_connection = DataBaseConnection()
