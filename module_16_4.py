from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List, Dict
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str = None
    age: int = None


@app.get("/users", response_model=List[User])
async def get_user_id() -> List[User]:
    return users


@app.post('/user/{username}/{age}', response_model=User)
async def create_user(
        username: Annotated[str, Path(min_length=3, max_length=12, description='Enter username', example='Paul')],
        age: Annotated[int, Path(ge=14, le=80, description='Enter age', example='20')]
):
    user_id = int(max([user.id for user in users], default=0)) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(
        user_id: Annotated[int, Path(ge=1, description='Enter user ID', example='1')],
        username: Annotated[str, Path(min_length=3, max_length=12, description='Enter username', example='Paul')],
        age: Annotated[int, Path(ge=14, le=80, description='Enter age', example='20')]) -> str:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id: Annotated[int, Path(ge=1, description='Enter user ID', example='1')]):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User  was not found")

# Команда для запуска приложения
# uvicorn module_16_4:app --reload
