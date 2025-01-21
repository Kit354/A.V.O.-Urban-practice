from module_17.backend.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from module_17.models import *


class User(Base):
    # Задает имя таблицы
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    # Создает столбец таблицы с уникальным номером
    id = Column(Integer, primary_key=True, index=True)

    # Создает столбцы таблицы
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)

    # Человеочитаемое название URL, если применить функцию slugify
    slug = Column(String, unique=True, index=True)

    # связь таблиц
    tasks = relationship('Task', back_populates='user')

# Визуализировать таблицу
# from sqlalchemy.schema import CreateTable
# print(CreateTable(User.__table__))
