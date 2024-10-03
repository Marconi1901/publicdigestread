import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建SQLAlchemy的基础类
Base = declarative_base()

# 定义书摘表
class Quote(Base):
    __tablename__ = 'digestbook'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(3000), nullable=False)
    bookname = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)

# MySQL数据库连接信息
DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/digestdemo"

# 创建数据库引擎
engine = create_engine(DATABASE_URL, echo=True)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 读取 quotes.json 文件
with open('quotes.json', 'r', encoding='utf-8') as file:
    quotes_data = json.load(file)

# 插入书摘数据到数据库，插入之前先校验
for quote in quotes_data:
    # 检查数据库中是否已经存在相同的书摘（根据 text 和 book 字段）
    existing_quote = session.query(Quote).filter_by(content=quote['content'], bookname=quote['bookname']).first()
    
    if existing_quote:
        print(f"书摘已存在，跳过插入: {quote['bookname']} - {quote['content']}")
    else:
        # 插入新的书摘
        new_quote = Quote(content=quote['content'], bookname=quote['bookname'], author=quote['author'])
        session.add(new_quote)
        print(f"插入新书摘: {quote['bookname']} - {quote['content']}")

# 提交事务
session.commit()

print("书摘数据已成功处理！")