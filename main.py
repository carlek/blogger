import asyncio
import strawberry
import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import declarative_base
from strawberry.fastapi import GraphQLRouter
from strawberry_classes.queries import Query
from strawberry_classes.mutations import Mutation
from util.async_objects import Engine
from util.settings import settings
from db.models import Base

# define FastAPI app
app = FastAPI()

# define GraphQL app with Strawberry schema
graphql_app = GraphQLRouter(schema=strawberry.Schema(query=Query, mutation=Mutation))

# mount GraphQL app to FastAPI app
app.include_router(graphql_app, prefix="/graphql")

async def init_models():
	engine = Engine().async_engine
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.drop_all)
		await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
	asyncio.run(init_models())
	uvicorn.run(app, port=settings.APP_PORT, host=settings.APP_HOST)

	pass
