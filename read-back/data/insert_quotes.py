import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 获取 app 目录的绝对路径
import sys
import os
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))
# 将 app 目录添加到 sys.path
sys.path.append(app_path)
# 导入 config 模块
from config import Config

# 创建SQLAlchemy的基础类
Base = declarative_base()

# 定义书摘表
class Quote(Base):
    __tablename__ = 'digestbook'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(3000), nullable=False)
    bookname = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)

# 创建数据库引擎 mysql+pymysql://user:password@localhost:3306/digestdemo
print(f"path:{Config.DATABASE_PY_URL}")
engine = create_engine(Config.DATABASE_PY_URL, echo=True)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

before_total = session.query(Quote).count()

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

after_total = session.query(Quote).count()
print(f"书摘数据已成功处理！处理前：{before_total},处理后：{after_total}，差异：{after_total-before_total}")