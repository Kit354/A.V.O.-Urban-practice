from fastapi import FastAPI, Path, HTTPException, Request, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Annotated
from pydantic import BaseModel

app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True}, debug=True)

templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get("/user/{user_id}")
async def get_user_id(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id]})
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.post('/{username}/{age}', status_code=status.HTTP_201_CREATED)
async def create_user(
        request: Request,
        username: Annotated[str, Path(min_length=3, max_length=12, description='Enter username', example='Mitya')],
        age: Annotated[int, Path(ge=14, le=80, description='Enter age', example='20')]
) -> HTMLResponse:
    if users:
        user_id = max(users, key=lambda m: m.id).id + 1
    else:
        user_id = 0
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(
        user_id: Annotated[int, Path(ge=1, description='Enter user ID', example='1')],
        username: Annotated[str, Path(min_length=3, max_length=12, description='Enter username', example='Sasha')],
        age: Annotated[int, Path(ge=14, le=80, description='Enter age', example='35')]) -> str:
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
# uvicorn module_16_5:app --reload
