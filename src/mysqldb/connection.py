from core import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DataBaseConnection:
    def __init__(self):
        self.engine = create_engine(settings.get_string_connection())
        self.db_session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)


db_connection = DataBaseConnection()
