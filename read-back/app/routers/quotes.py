from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas, models
from app.database import get_session
from typing import List

router = APIRouter(
    prefix="/quotes",  # 给所有的路由添加前缀
    tags=["Quotes"],   # 路由组标签
)

# 获取所有书摘
@router.get("/", response_model=List[schemas.BookQuoteRead])
async def get_quotes(session: AsyncSession = Depends(get_session)):
    return await crud.get_quotes(session)

# 随机获取指定条数书摘
@router.get("/random/{limit}", response_model=List[schemas.BookQuoteRead])
async def get_random_quotes(limit: int,session: AsyncSession = Depends(get_session)):
    return await crud.get_random_quotes(session, limit)

# 创建书摘
@router.post("/", response_model=schemas.BookQuoteRead)
async def create_quote(quote: schemas.BookQuoteCreate, session: AsyncSession = Depends(get_session)):
    return await crud.create_quote(session, quote)

# 获取单个书摘
@router.get("/{quote_id}", response_model=schemas.BookQuoteRead)
async def get_quote(quote_id: int, session: AsyncSession = Depends(get_session)):
    return await crud.get_quote(session, quote_id)

# 更新书摘
@router.put("/{quote_id}", response_model=schemas.BookQuoteRead)
async def update_quote(quote_id: int, updated_quote: schemas.BookQuoteCreate, session: AsyncSession = Depends(get_session)):
    return await crud.update_quote(session, quote_id, updated_quote)

# 删除书摘
@router.delete("/{quote_id}")
async def delete_quote(quote_id: int, session: AsyncSession = Depends(get_session)):
    return await crud.delete_quote(session, quote_id)

# 获取书摘总数
@router.get("/get/total", response_model=schemas.BookQuoteTotal)
async def get_quotes_total(session: AsyncSession = Depends(get_session)):
    total_quotes = await crud.get_quotes_total(session)
    return {"total_quotes": total_quotes}