import pytest
from strawberry_classes.mutations import Mutation
from strawberry_classes.queries import Query

query = Query()
mutation = Mutation()

# @pytest.mark.asyncio
# async def test_create_author(url, headers, clear_tables):
# 	result = await mutation.create_author(username="JaneDoe", email="janedoe@mail.com", password="password456")
# 	assert result

@pytest.mark.asyncio
async def test_get_author():
	result = await query.get_author(1)
	assert result.username == "johndoe"
	assert result.email == "johndoe@example.com"
	assert result.password == "password123"
