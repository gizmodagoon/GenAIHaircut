from pydantic import BaseModel

class HaircutCreate(BaseModel):
    style: str

class HaircutOut(HaircutCreate):
    id: int

    class Config:
        from_attributes = True
