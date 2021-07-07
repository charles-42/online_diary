import sys
sys.path.insert(0, "/Users/charles/github/online_diary")
import mysql.connector
from src.config import mysql_user, mysql_mdp


def call_connector(db="none"):
    """ Function which connects to MySQL """
    if db=="none":
        db_connection = mysql.connector.connect(
        host="localhost",
        user=mysql_user,
        passwd = mysql_mdp)
    else:
        db_connection = mysql.connector.connect(
        host="localhost",
        user=mysql_user,
        passwd = mysql_mdp,
        database=db)
    db_cursor = db_connection.cursor(buffered=True, dictionary=False)
    return db_connection, db_cursor
