from module_17.backend.db import SessionLocal


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
