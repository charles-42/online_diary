
import sys
sys.path.insert(0, "/Users/charles/github/online_diary")
import mysql.connector
from src.utils.functions import *

### Creation of our database named "Diary_db"

# Creation of the database 'Diary_db' if it does not exists

def create_db_Diary_if_not_exist():
    # Connection with MySQL
    db_connection, db_cursor = call_connector()
    try:
         db_cursor.execute("CREATE DATABASE IF NOT EXISTS Diary_db")
    except ProgrammingError as progErr:
         print("La database n'existe pas !")
    db_connection.commit()


### Displaying databases

def display_db():
    # Connection with MySQL
    db_connection, db_cursor = call_connector()
    db_cursor.execute("SHOW DATABASES") # Displaying of our databases

    for db in db_cursor:
    	print(db) # Printing of all the databases


# Creation of the table 'text' if it does not exists
def create_text_if_not_exist():
    # Connection with MySQL
    db_connection, db_cursor = call_connector()
    db_cursor.execute("USE Diary_db; ")
    create_text_table = """
    CREATE TABLE IF NOT EXISTS text(
        text_date DATE NOT NULL PRIMARY KEY,
        text_content VARCHAR(500) NOT NULL
        )
        """
    db_cursor.execute(create_text_table)
    db_connection.commit()



if __name__ == "__main__":
    create_db_Diary_if_not_exist()
    display_db()
    create_text_if_not_exist()
