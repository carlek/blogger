from strawberry_classes.mutations import Mutations
from strawberry_classes.models import AuthorSuccess, AuthorResponse
from strawberry_classes.models import PostSuccess, PostResponse
from strawberry_classes.models import PostCommentSuccess, PostCommentResponse

mutation = Mutations()

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

async def create_test_post_comment() -> PostCommentResponse:
	await create_test_post()
	result = await mutation.create_post_comment(post_id=1, author_id=1, content="postcomment content")
	assert type(result) == PostCommentSuccess
	assert result.message == "PostComment created"
