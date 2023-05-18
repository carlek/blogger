import pytest
from strawberry_classes.mutations import Mutation
from strawberry_classes.queries import Query
from strawberry_classes.models import PostCommentSuccess, Error
from .utils import clear_tables, create_test_post_comment, create_test_post

query = Query()
mutation = Mutation()

@pytest.mark.asyncio
async def test_create_post_comment():
	await clear_tables()
	await create_test_post()
	result = await mutation.create_post_comment(post_id=1, author_id=1, content="comment on post#1 -author#1")
	assert type(result) == PostCommentSuccess
	assert result.message == "PostComment created"
	result = await mutation.create_post_comment(post_id=1, author_id=2, content="comment on post#1 -bad author")
	assert type(result) == Error
	assert "foreign key constraint" in result.message
	result = await mutation.create_post_comment(post_id=2, author_id=1, content="comment on bad post -author#1")
	assert type(result) == Error
	assert "foreign key constraint" in result.message

@pytest.mark.asyncio
async def test_get_post_comment():
	await clear_tables()
	await create_test_post_comment()
	result = await query.get_post_comment(1)
	assert type(result) == PostCommentSuccess
	assert result.postcomment.content == "postcomment content"
	assert result.message == "PostComment with id=1 found"
	result = await query.get_post_comment(999)
	assert type(result) == Error
	assert "not found" in result.message


@pytest.mark.asyncio
async def test_edit_post_comment():
	await clear_tables()
	await create_test_post_comment()
	result = await query.get_post_comment(1)
	created = result.postcomment.created_at
	result = await mutation.edit_post_comment(id=1, content="new content")
	assert type(result) == PostCommentSuccess
	assert result.postcomment.content == "new content"
	assert result.postcomment.created_at == created
	assert result.postcomment.created_at < result.postcomment.updated_at
	result = await mutation.edit_post(id=2, content="new content",  title="new title")
	assert type(result) == Error
	assert result.message == "Post not found, not edited: id = 2"

@pytest.mark.asyncio
async def test_delete_post_comment():
	await clear_tables()
	await create_test_post_comment()
	result = await mutation.delete_post_comment(id=1)
	assert result.message == "PostComment deleted successfully"
	result = await mutation.delete_post_comment(id=2)
	assert type(result) == Error
	assert result.message == "PostComment not found, not deleted: id=2"
