import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry_classes.queries import Queries
from strawberry_classes.mutations import Mutations
import fastapi
from db.utils import create_data

# define FastAPI app
app = fastapi.FastAPI()

# define GraphQL app with Strawberry schema and add route
graphql_app = GraphQLRouter(schema=strawberry.Schema(query=Queries, mutation=Mutations))
app.include_router(graphql_app, prefix="/graphql")


class ApiError(Exception):
	def __init__(self, error_msg: str, status_code: int):
		super().__init__(error_msg)
		self.status_code = status_code
		self.error_msg = error_msg


# REST api to populate database
@app.post('/populate-database/')
def populate_database():
	try:
		create_data()
		return fastapi.Response(content="Database populated", status_code=200)
	except ApiError as e:
		return fastapi.Response(content=e.error_msg, status_code=e.status_code)
	except Exception as x:
		return fastapi.Response(content=str(x), status_code=500)
