import pytest
from strawberry_classes.mutations import Mutation
from strawberry_classes.queries import Query
from strawberry_classes.models import Author
from strawberry_classes.models import AuthorSuccess, Error
from conftest import clear_tables

query = Query()
mutation = Mutation()

@pytest.mark.asyncio
async def test_create_author():
	await clear_tables()
	result = await mutation.create_author(username="oscar", email="oscar@grouch.com", password="goaway!!!")
	assert type(result) == AuthorSuccess
	assert result.message == "Author created"

@pytest.mark.asyncio
async def test_get_author():
	await test_create_author()
	result = await query.get_author(1)
	assert type(result) == Author
	assert result.username == "oscar"
	assert result.email == "oscar@grouch.com"
	assert result.password == "goaway!!!"

@pytest.mark.asyncio
async def test_edit_author():
	await test_create_author()
	result = await query.get_author(1)
	created = result.created_at
	result = await mutation.edit_author(id=1, username="newoscar", email="newoscar@grouch.com", password="newpassword")
	assert type(result) == AuthorSuccess
	assert result.author.username == "newoscar"
	assert result.author.email == "newoscar@grouch.com"
	assert result.author.password == "newpassword"
	assert result.author.created_at == created
	assert result.author.created_at < result.author.updated_at
	result = await mutation.edit_author(id=2, username="newoscar", email="newoscar@grouch.com", password="newpassword")
	assert type(result) == Error
	assert result.message == 'Author with id 2 not found'

@pytest.mark.asyncio
async def test_delete_author():
	await test_create_author()
	result = await mutation.delete_author(id=1)
	assert result.message == "Author deleted successfully"
	result = await mutation.delete_author(id=2)
	assert type(result) == Error
	assert result.message == "Author not found, not deleted: id=2"
