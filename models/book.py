from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base
from models.category import Category


class Book(Base):
    __tablename__ = 'book'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    category_id: Mapped[int] = mapped_column(ForeignKey(Category.id))
