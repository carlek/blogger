import asyncio
import strawberry
import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base
from strawberry.fastapi import GraphQLRouter
from strawberry_classes.queries import Query
from strawberry_classes.mutations import Mutation
from util.settings import settings

# define FastAPI app
app = FastAPI()

# define GraphQL app with Strawberry schema
graphql_app = GraphQLRouter(schema=strawberry.Schema(query=Query, mutation=Mutation))

# mount GraphQL app to FastAPI app
app.include_router(graphql_app, prefix="/graphql")

async def init_models():
	base = declarative_base()
	async with engine.begin() as conn:
		# await conn.run_sync(base.metadata.drop_all)
		await conn.run_sync(base.metadata.create_all)

global engine, SessionLocal

if __name__ == "__main__":
	# create engine and session
	engine = create_async_engine(url=settings.DB_CONNECTION_STR, echo=True)
	SessionLocal = AsyncSession(bind=engine)

	# initialize models and run app
	asyncio.run(init_models())
	uvicorn.run(app, port=settings.APP_PORT, host=settings.APP_HOST)

	pass
