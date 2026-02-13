from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ai.haircut_analyzer_agent import get_haircut_analysis
from db.crud import db_create_haircut, db_get_haircuts
from db.schemas import HaircutCreate, HaircutOut
from db.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

class AnalyzeHaircutRequest(BaseModel):
    image: str   

@router.post("/haircuts/analyze")
def analyze_haircut(query: AnalyzeHaircutRequest):
    """
    Analyze a haircut query using Claude AI.
    
    Request body should contain a 'image' field with represents the haircut to analyze.
    """
    result = get_haircut_analysis(query.image)
    return result


@router.post("/haircuts", response_model=HaircutOut)
async def create_haircut(haircut: HaircutCreate, db: AsyncSession = Depends(get_db)):
    return await db_create_haircut(db, haircut)


@router.get("/haircuts", response_model=list[HaircutOut])
async def get_haircuts(db: AsyncSession = Depends(get_db)):
    return await db_get_haircuts(db)
