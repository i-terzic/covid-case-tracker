"""Database utility connection"""
import os
from pathlib import Path

import pymssql
from dotenv import load_dotenv

load_dotenv()
env_path = Path('..')/'.env'

load_dotenv(dotenv_path=env_path)


class DatabaseConnection():
    """Context Manager for mssql db connection"""

    def __init__(self) -> None:
        """get db connection config"""
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PWRD = os.getenv('DB_PWRD')
        self.conn = None
        self.cur = None

    def __enter__(self) -> 'pymssql.connection.cursor':
        """return a cursor"""
        try:
            self.conn = pymssql.connect(
                server=self.DB_HOST,
                user=self.DB_USER,
                password=self.DB_PWRD,
                database=self.DB_NAME,
                timeout=3)
            self.cur = self.conn.cursor(as_dict=True)
            return self.cur
        except RuntimeError as err:
            raise err

    def __exit__(self, _type, value, traceback) -> None:
        """commit everything, close cursor and close connection"""
        self.conn.commit()
        self.cur.close()
        self.conn.close()
