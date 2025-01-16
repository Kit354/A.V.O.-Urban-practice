from fastapi import APIRouter


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
