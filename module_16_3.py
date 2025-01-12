from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_user_id() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def append_user(
        username: Annotated[str, Path(min_length=3, max_length=12, description='Enter username', example='Paul')],
        age: Annotated[int, Path(ge=14, le=80, description='Enter age', example='20')]) -> str:
    user_id = str(int(max(users, key=int)) + 1 if users else 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=1, description='Enter user ID', example='1')],
        username: Annotated[str, Path(min_length=3, max_length=12, description='Enter username', example='Paul')],
        age: Annotated[int, Path(ge=14, le=80, description='Enter age', example='20')]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, description='Enter user ID', example='1')]):
    user_id_str = str(user_id)
    if user_id_str in users:
        del users[user_id_str]
        return f'User {user_id} has been deleted'
    else:
        return f'User {user_id} not found'

# Команда для запуска приложения
# uvicorn module_16_3:app --reload
