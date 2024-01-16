from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int]
    name: Mapped[str]
    nickname: Mapped[str]
