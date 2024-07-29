import os
import sys
import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from conf import Config


Base = declarative_base()


class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    telegram_uid = Column(String(250), nullable=True)
    email = Column(String(250), nullable=True)
    phone = Column(String(30), nullable=True)


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), primary_key=True)
    player_id = Column(Integer, ForeignKey('player.id'))
    points = Column(Integer, nullable=True)
    player = relationship(Player)


class Session(Base):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship(Group)
    started = Column(DateTime, default=datetime.datetime.utcnow)
    ended = Column(DateTime)


engine = create_engine(Config.DATABASE_URL)

Base.metadata.create_all(engine)
