from fastapi import FastAPI
from app.routers import quotes  # 导入 quotes 路由

app = FastAPI()

# 包含各个模块的路由
app.include_router(quotes.router)

# 启动时执行的操作，例如数据库连接
@app.on_event("startup")
async def startup():
    print("Application starting...")

@app.on_event("shutdown")
async def shutdown():
    print("Application shutting down...")
