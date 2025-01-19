from fastapi import APIRouter, Depends, status, HTTPException

# Сессия БД
from sqlalchemy.orm import Session

# Функция подключения к БД
from module_17.backend.db_depends import get_db

# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from module_17.models.user import User
from module_17.schemas import CreateUser, UpdateUser

# Функции работы с записями.
from sqlalchemy import insert, select, update, delete

# Функция создания slug-строки
from slugify import slugify

router_user = APIRouter(prefix='/user', tags=['user'])


@router_user.get('/all_users')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router_user.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user:
        return user
    raise HTTPException(status_code=404,
                        detail='User was not found')


@router_user.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_new_user: CreateUser):
    db.execute(insert(User).values(username=create_new_user.username,
                                   firstname=create_new_user.firstname,
                                   lastname=create_new_user.lastname,
                                   age=create_new_user.age,
                                   slug=create_new_user.username))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}


@router_user.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, updates_user: UpdateUser):
    user_update = db.scalar(select(User).where(User.id == user_id))
    if user_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='There is no user found!')
    db.execute(update(User).where(User.id == user_id).values(firstname=updates_user.username,
                                                             lastname=updates_user.lastname,
                                                             age=updates_user.age))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'detail': 'User update is successful!'}


@router_user.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user_delete = db.scalar(select(User).where(User.id == user_id))
    if user_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='There is no user found')
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'User delete is successful!'}
