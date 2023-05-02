
from util.settings import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

# Singleton class: only one object
class Engine:
	_instance = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super(Engine, cls).__new__(cls)
			async_engine = create_async_engine(url=settings.DB_CONNECTION_STR, echo=True)
			cls.SessionLocal = AsyncSession(bind=async_engine)
			cls.engine = async_engine
		return cls._instance
