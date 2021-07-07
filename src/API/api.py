import sys
sys.path.insert(0, "/Users/charles/github/online_diary")

import uvicorn
from fastapi import FastAPI, Form
from src.utils.functions import *
from src.API.classes import *
from datetime import date

#API initialization
app = FastAPI()


### Text requests

# Request to add a new text

@app.post("/text") #HTTP verb is post
def create_text(entry_text:Text): # The parameter Text is a class
    db_connection, db_cursor = call_connector(db="Diary_db") #connection with db

    #define and execute the query
    query = """ INSERT INTO text (
                text_date, text_content)
                values (%s,%s)
            """
    values=[(entry_text.text_date,entry_text.text_content)]
    db_cursor.executemany(query,values)

    #save changes into the db
    db_connection.commit()
    return {"text_date" : entry_text.text_date, "text_content" : entry_text.text_content}

# Requête pour modify a text

@app.put("/text")
def modify_text(modify_text : Text):
    db_connection, db_cursor = call_connector(db="Diary_db")
    query = """ UPDATE text
                SET text_content = %s
                WHERE text_date= %s;
            """

    values=[(modify_text.text_content,modify_text.text_date)]

    db_cursor.executemany(query,values)
    db_connection.commit()
    return {"text_date" : modify_text.text_date, "new_text" : modify_text.text_content}

# Request to read a text

@app.get("/text")
def get_text(get_text : Text):
    db_connection, db_cursor = call_connector(db="Diary_db")
    query = """ SELECT text_content
                FROM text
                WHERE text_date= %s;
            """
    values = [(get_text.text_date,)] # %s is always replace by a tuple
    db_cursor.executemany(query,values)

    # a get operation does modify the db so no need for "commit"

    return db_cursor.fetchall()

# Request to delete a text

@app.delete("/text")
def delete_text(delete_text:Text):
    db_connection, db_cursor = call_connector(db="Diary_db")
    query = """ DELETE FROM text
                WHERE text_date= %s;
            """
    values = [(delete_text.text_date,)]
    db_cursor.executemany(query,values)
    db_connection.commit()
    return "text deleted"

#When we call this file from the terminal, the api is automaticaly launched
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)
