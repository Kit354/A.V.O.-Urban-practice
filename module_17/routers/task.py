from fastapi import APIRouter, Depends, status, HTTPException

# Сессия БД
from sqlalchemy.orm import Session

# Функция подключения к БД
from module_17.backend.db_depends import get_db

# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from module_17.models.task import Task
from module_17.schemas import CreateTask, UpdateTask

# Функции работы с записями.
from sqlalchemy import insert, select, update, delete

# Функция создания slug-строки
from slugify import slugify


router_task = APIRouter(prefix='/task', tags=['task'])


@router_task.get('/all_tasks')
async def all_tasks():
    pass


@router_task.get('/task_id')
async def task_by_id():
    pass


@router_task.post('/create')
async def create_task():
    pass


@router_task.put('/update')
async def update_tasks():
    pass


@router_task.delete('/delete')
async def delete_tasks():
    pass
