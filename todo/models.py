from sqlalchemy import Column, Integer, String, Boolean
from todo.database import Base

class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    completed = Column(Boolean)

    def __init__(self, text=None):
        self.text = text

    def __repr__(self):
        return "<Entry: {}>".format(self.text)
