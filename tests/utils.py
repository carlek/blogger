from strawberry_classes.mutations import Mutation
from strawberry_classes.models import AuthorSuccess, AuthorResponse
from strawberry_classes.models import PostSuccess, PostResponse

mutation = Mutation()

async def clear_tables() -> None:
	result = await mutation.truncate_table("author")
	assert result == "success"
	result = await mutation.truncate_table("post")
	assert result == "success"
	result = await mutation.truncate_table("postcomment")
	assert result == "success"

async def create_test_author() -> AuthorResponse:
	result = await mutation.create_author(username="oscar", email="oscar@grouch.com", password="goaway!!!")
	assert type(result) == AuthorSuccess
	assert result.message == "Author created"

async def create_test_post() -> PostResponse:
	await create_test_author()
	result = await mutation.create_post(title="post title", content="post content", author_id=1)
	assert type(result) == PostSuccess
	assert result.message == "Post created"
