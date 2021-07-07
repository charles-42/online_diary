import sys
sys.path.insert(0, "/Users/charles/github/online_diary")
import pytest
import asyncio
from src.utils.functions import *


#from httpx import AsyncClient
#from src.API.api import app

from src.config import mysql_user, mysql_mdp


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

# We create a fixture is a kinf of simulated coding frame
# The first fixture we want to create is a simulated Database

@pytest.mark.asyncio
@pytest.fixture(scope='module') #fixture is at module level: it will be run only once
async def create_db(event_loop):
    print("Creating db")
    db_connection, db_cursor = call_connector()
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS Diary_db")
    db_cursor.execute("USE Diary_db")

    create_text_table = """
    CREATE TABLE IF NOT EXISTS text(
         text_date DATE NOT NULL PRIMARY KEY,
         text_content VARCHAR(500) NOT NULL
    )
    """

    db_cursor.execute(create_text_table)

    populate_table = """
    INSERT INTO text(text_date,text_content)
    VALUES("2015-08-03","bonne journée")
    """
    db_cursor.execute(populate_table)
    db_connection.commit()

    yield db_cursor  # variables sent to tests

    print("Destroying db")
    db_connection, db_cursor = call_connector()
    db_cursor.execute("DROP DATABASE Diary_db")
    db_connection.commit()

# We now create a second fixture, a simulated app which use our simulated db
# @pytest.mark.asyncio
# @pytest.fixture(scope='module') #fixture is at module level: it will be run only once
# async def create_test_app(create_db):
#     ac=AsyncClient(app=app, base_url="http://test")
