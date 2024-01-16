from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class Category(Base):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
