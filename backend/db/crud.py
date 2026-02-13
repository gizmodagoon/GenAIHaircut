from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models import Haircut
from .schemas import HaircutCreate

async def db_create_haircut(db: AsyncSession, haircut: HaircutCreate):
    new_haircut = Haircut(**haircut.model_dump())
    db.add(new_haircut)
    await db.commit()
    await db.refresh(new_haircut)
    return new_haircut

async def db_get_haircuts(db: AsyncSession):
    result = await db.execute(select(Haircut))
    return result.scalars().all()
