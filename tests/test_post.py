import pytest
from strawberry_classes.mutations import Mutations
from strawberry_classes.queries import Queries
from strawberry_classes.models import PostSuccess, Error
from .utils import clear_tables, create_test_author, create_test_post

query = Queries()
mutation = Mutations()

@pytest.mark.asyncio
async def test_create_post():
	await clear_tables()
	await create_test_author()
	result = await mutation.create_post(title="Title: Post #1 by author:1",
										content="this is #1 -author:1",
										author_id=1)
	assert type(result) == PostSuccess
	assert result.message == "Post created"
	result = await mutation.create_post(title="Title: by non-existing author:2",
										content="this is from non-exist author:2",
										author_id=2)
	assert type(result) == Error
	assert "foreign key constraint" in result.message

@pytest.mark.asyncio
async def test_get_post():
	await clear_tables()
	await create_test_post()
	result = await query.get_post(1)
	assert type(result) == PostSuccess
	assert result.post.title == "post title"
	assert result.post.content == "post content"
	assert result.post.created_at == result.post.updated_at
	assert result.message == "Post with id=1 found"
	result = await query.get_post(999)
	assert type(result) == Error
	assert "not found" in result.message


@pytest.mark.asyncio
async def test_edit_post():
	await clear_tables()
	await create_test_post()
	result = await query.get_post(1)
	created = result.post.created_at
	result = await mutation.edit_post(id=1, content="new content",  title="new title")
	assert type(result) == PostSuccess
	assert result.post.content == "new content"
	assert result.post.title == "new title"
	assert result.post.created_at == created
	assert result.post.created_at < result.post.updated_at
	result = await mutation.edit_post(id=2, content="new content",  title="new title")
	assert type(result) == Error
	assert result.message == "Post not found, not edited: id = 2"

@pytest.mark.asyncio
async def test_delete_post():
	await clear_tables()
	await create_test_post()
	result = await mutation.delete_post(id=1)
	assert result.message == "Post deleted successfully"
	result = await mutation.delete_post(id=2)
	assert type(result) == Error
	assert result.message == "Post not found, not deleted: id=2"
