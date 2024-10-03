from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import func
from app.models import BookQuote
from app.schemas import BookQuoteCreate

# 获取所有书摘
async def get_quotes(session: AsyncSession):
    result = await session.execute(select(BookQuote))
    return result.scalars().all()

# 获取书摘总数
async def get_quotes_total(session: AsyncSession) -> int:
    result = await session.execute(func.count(BookQuote.id))
    return result.scalar()

# 随机获取指定条数书摘
async def get_random_quotes(session: AsyncSession, limit: int):
    total_count = await session.scalar(select(func.count()).select_from(BookQuote))
    random_offset = await session.scalar(select(func.floor(func.random() * (total_count - limit))))
    result = await session.execute(select(BookQuote).offset(random_offset).limit(limit))
    return result.scalars().all()

# 获取单个书摘
async def get_quote(session: AsyncSession, quote_id: int):
    return await session.get(BookQuote, quote_id)

# 创建书摘
async def create_quote(session: AsyncSession, quote: BookQuoteCreate):
    new_quote = BookQuote(content=quote.content, bookname=quote.bookname, author=quote.author)
    session.add(new_quote)
    await session.commit()
    await session.refresh(new_quote)
    return new_quote

# 更新书摘
async def update_quote(session: AsyncSession, quote_id: int, updated_quote: BookQuoteCreate):
    quote = await session.get(BookQuote, quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    quote.content = updated_quote.content
    quote.bookname = updated_quote.bookname
    quote.author = updated_quote.author
    await session.commit()
    await session.refresh(quote)
    return quote

# 删除书摘
async def delete_quote(session: AsyncSession, quote_id: int):
    quote = await session.get(BookQuote, quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    await session.delete(quote)
    await session.commit()
    return {"detail": "Quote deleted successfully"}