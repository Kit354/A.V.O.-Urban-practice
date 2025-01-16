from fastapi import APIRouter


router_user = APIRouter(prefix='/user', tags=['user'])


@router_user.get('/all_users')
async def all_users():
    pass


@router_user.get('/user_id')
async def user_by_id():
    pass


@router_user.post('/create')
async def create_user():
    pass


@router_user.put('/update')
async def update_user():
    pass


@router_user.delete('/delete')
async def delete_user():
    pass
