from pydantic import BaseModel

class BookQuoteCreate(BaseModel):
    content: str
    bookname: str
    author: str

# 返回书摘总数的模型
class BookQuoteTotal(BaseModel):
    total_quotes: int

class BookQuoteRead(BaseModel):
    id: int
    content: str
    bookname: str
    author: str

    class Config:
        orm_mode = True
