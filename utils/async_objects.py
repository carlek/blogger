
from util.settings import settings
from sqlalchemy.ext.asyncio import create_async_engine

# Singleton class, we only need one of these...
class Engine:
	_instance = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super(Engine, cls).__new__(cls)
			cls.async_engine = create_async_engine(url=settings.DB_CONNECTION_STR, echo=True)
		return cls._instance
