import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

class Config:
    # 从 .env 文件中读取数据库连接信息
    DATABASE_URL = os.getenv('DATABASE_URL', 'mysql+pymysql://user:password@localhost/db_name')