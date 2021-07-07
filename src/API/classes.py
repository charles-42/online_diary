from pydantic import BaseModel
from typing import Optional
import datetime

class Text(BaseModel):
    #text_date is the primary key so it's compulsory
    text_date: str

    #When you do a "get" you don't know the text_content: it has to be Optional
    text_content: Optional[str] = None
