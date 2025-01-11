from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_root() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def get_admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_user_id(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def route_to_users(username: str, age: int = 0) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


# Команда для запуска приложения
# uvicorn module_16_1:app --reload
