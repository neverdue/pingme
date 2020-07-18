from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from create import Base, db_session
from sqlalchemy.orm import sessionmaker, relationship


class User(UserMixin, Base):
    """ User model """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True, nullable=False)
    hashed_pswd = Column(String(), nullable=False)

    def __init__(self, username, hashed_pswd):
        self.username = username
        self.hashed_pswd = hashed_pswd

    def __repr__(self):
        return '<User %r>' % (self.name)
