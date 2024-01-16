from sqlalchemy import select
from connection.db import Session_book
from models.book import Book
from models.category import Category


class MessageController():
    session = Session_book
    @classmethod
    def get_book_by_categories(cls, category):
        request = select(Book.name).select_from(Book).join(Category, Category.id == Book.category_id).where(Category.name == category)
        with cls.session.begin() as session:
            return session.execute(request).scalars().all()
