from fastapi import APIRouter, Depends, status, HTTPException

# Сессия БД
from sqlalchemy.orm import Session

# Функция подключения к БД
from module_17.backend.db_depends import get_db

# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from module_17.models import *
from module_17.schemas import CreateTask, UpdateTask

# Функции работы с записями.
from sqlalchemy import insert, select, update, delete

# Функция создания slug-строки
from slugify import slugify

router_task = APIRouter(prefix='/task', tags=['task'])


@router_task.get('/all_tasks')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router_task.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    current_task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if current_task:
        return current_task
    raise HTTPException(status_code=404,
                        detail='Task was not found')


@router_task.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_new_task: CreateTask, user_id: int):
    current_user = db.scalars(select(User).where(User.id == user_id)).first()
    if current_user is None:
        raise HTTPException(status_code=404,
                            detail='User was not found')
    db.execute(insert(Task).values(title=create_new_task.title,
                                   content=create_new_task.content,
                                   priority=create_new_task.priority,
                                   user_id=user_id,
                                   slug=create_new_task.title))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}


@router_task.put('/update')
async def update_tasks(db: Annotated[Session, Depends(get_db)], task_id: int, updates_task: UpdateTask):
    task_update = db.scalar(select(Task).where(Task.id == task_id))
    if task_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='There is no user found!')
    db.execute(update(Task).where(Task.id == task_id).values(title=updates_task.title,
                                                             content=updates_task.content,
                                                             priority=updates_task.priority,
                                                             slug=updates_task.title))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'detail': 'User update is successful!'}


@router_task.delete('/delete')
async def delete_tasks(db: Annotated[Session, Depends(get_db)], task_id: int):
    task_delete = db.scalar(select(Task).where(Task.id == task_id))
    if task_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='There is no user found')
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'User delete is successful!'}
