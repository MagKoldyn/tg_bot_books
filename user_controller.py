from sqlalchemy import select, insert
from telebot.types import User as tgUser

from connection.db import Session_book
from models.user import User


class UserController():
    session = Session_book

    def get_user_controller(self, from_user: tgUser):
        tgid = from_user.id
        first_name = from_user.first_name
        last_name = from_user.last_name
        username = from_user.username
        if not self.check_user(tgid):
            user_info = dict(tgid=tgid, first_name=first_name, last_name=last_name, username=username)
        self.insert_user(user_info)
        nickname = first_name + ' ' + last_name
        return nickname

    def check_user(self, tgid):
        query = select(all).select_from(User).where(tgid == User.id)
        with self.session.begin() as session:
            user1 = session.execute(query).all()
            return user1 is not None
            # return session.execute(query).all()
            # print(session.execute(query).all())

    def insert_user(self, user_info):
        query = insert(User).values(user_info)
        with self.session.begin() as session:
            session.execute(query)
            session.commit()
