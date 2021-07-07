import pytest
import sys
from mysql.connector import IntegrityError

def test_acces_db(create_db):
    create_db.execute("SELECT * from text")
    rs = create_db.fetchall()
    assert len(rs)==1


# The database primarly contains 1 instance so we just test the Connection
def test_double_date(create_db):
    create_db.execute("INSERT INTO text(text_date,text_content) VALUES('2001-01-01','bonne journée')")

    with pytest.raises(IntegrityError):
        create_db.execute("INSERT INTO text(text_date,text_content) VALUES('2001-01-01','sale journée')")
