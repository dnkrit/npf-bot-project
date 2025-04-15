
import asyncpg
from config import DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT

async def create_pool():
    return await asyncpg.create_pool(
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        host=DB_HOST,
        port=DB_PORT
    )
