from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .db import Base

class Haircut(Base):
    __tablename__ = "haircuts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    style: Mapped[str] = mapped_column(String)