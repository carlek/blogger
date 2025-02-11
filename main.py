import asyncio
import uvicorn

from utils.async_objects import Engine
from utils.settings import settings
from db.models import Base
from db.utils import create_fresh_database
from api.routes import app


async def init_models():
	engine = Engine().async_engine
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.drop_all)
		await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
	create_fresh_database()
	asyncio.run(init_models())
	uvicorn.run(app, port=settings.APP_PORT, host=settings.APP_HOST)
