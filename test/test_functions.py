import sys
sys.path.insert(0, "/Users/charles/github/online_diary")
from src.utils.functions import *


# Test the connexion to db.
def test_call_connector():
    db_connection, db_cursor = call_connector()
    assert isinstance(db_connection ,mysql.connector.connection.MySQLConnection)
