from module_17.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from module_17.models import *


class Task(Base):
    # Задает имя таблицы
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}

    # Создает столбец таблицы с уникальным номером
    id = Column(Integer, primary_key=True, index=True)

    # Создает столбцы таблицы
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True, index=True)

    # Человеочитаемое название URL, если применить функцию slugify
    slug = Column(String, unique=True, index=True)

    # связь таблиц
    user = relationship('User', back_populates='tasks')

# Визуализировать таблицу
# from sqlalchemy.schema import CreateTable
# print(CreateTable(Task.__table__))
