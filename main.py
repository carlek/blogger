import asyncio
import strawberry
import uvicorn
import fastapi
from strawberry.fastapi import GraphQLRouter
from strawberry_classes.queries import Query
from strawberry_classes.mutations import Mutation
from util.async_objects import Engine
from util.settings import settings
from db.models import Base
from db.utils import create_fresh_database, create_data

# define FastAPI app
app = fastapi.FastAPI()

# define GraphQL app with Strawberry schema and add route
graphql_app = GraphQLRouter(schema=strawberry.Schema(query=Query, mutation=Mutation))
app.include_router(graphql_app, prefix="/graphql")

@app.post('/populate-database/')
def populate_database():
	print("Populating database...")
	create_data()
	print("....Database populated")

async def init_models():
	engine = Engine().async_engine
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.drop_all)
		await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
	# asyncio.run(create_fresh_database(settings.DB_CONNECTION_STR))
	create_fresh_database("postgresql://carlek:ekekek@localhost:5432/blogger")
	asyncio.run(init_models())
	uvicorn.run(app, port=settings.APP_PORT, host=settings.APP_HOST)
