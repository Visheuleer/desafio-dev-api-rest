from pathlib import Path
import dotenv
import os

class Settings:
    def __init__(self):
        dotenv.load_dotenv(
            dotenv_path= os.path.join(Path(__file__).resolve().parent.parent.parent, '.config', '.env')
        )
        self._string_connection = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"


    def get_string_connection(self):
        return self._string_connection


settings = Settings()
