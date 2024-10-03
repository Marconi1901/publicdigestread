from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BookQuote(Base):
    __tablename__ = "digestbook"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(3000), nullable=False)
    bookname = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)