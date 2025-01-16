from fastapi import FastAPI
from module_17.routers import user, task


app = FastAPI()


@app.get('/')
async def home():
    return {'message': 'Welcome to Taskmanager'}


app.include_router(user.router_user)
app.include_router(task.router_task)

# Команда для запуска приложения
# python -m uvicorn module_17.main:app
