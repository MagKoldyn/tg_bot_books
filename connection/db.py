from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5432/user_books')
# engine = create_engine('postgresql+psycopg2://postgres@localhost:5432/test',echo=True,)


Session_book = sessionmaker(engine)