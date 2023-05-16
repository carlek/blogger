import pytest
from strawberry_classes.mutations import Mutation
from strawberry_classes.queries import Query
from strawberry_classes.models import Author

query = Query()
mutation = Mutation()

async def clear_tables() -> None:
	result = await mutation.truncate_table("author")
	assert result == "success"
	result = await mutation.truncate_table("post")
	assert result == "success"
	result = await mutation.truncate_table("postcomment")
	assert result == "success"

@pytest.mark.asyncio
async def test_create_author():
	await clear_tables()
	result = await mutation.create_author(username="oscar", email="oscar@grouch.com", password="goaway!!!")
	assert type(result) == Author

@pytest.mark.asyncio
async def test_get_author():
	await test_create_author()
	result = await query.get_author(1)
	assert type(result) == Author
	assert result.username == "oscar"
	assert result.email == "oscar@grouch.com"
	assert result.password == "goaway!!!"
