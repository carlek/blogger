import strawberry
from datetime import datetime

@strawberry.type
class Author:
	id: int
	username: str
	email: str
	password: str
	created_at: datetime
	updated_at: datetime

@strawberry.type
class Post:
	id: int
	title: str
	content: str
	author_id: int
	created_at: datetime
	updated_at: datetime

@strawberry.type
class PostComment:
	id: int
	post_id: int
	author_id: int
	content: str
	created_at: datetime
	updated_at: datetime

@strawberry.type
class AuthorSuccess:
	author: Author
	message: str

@strawberry.type
class PostSuccess:
	post: Post
	message: str

@strawberry.type
class PostCommentSuccess:
	postcomment: PostComment
	message: str

@strawberry.type
class Error:
	message: str


AuthorResponse = strawberry.union("AuthorResponses", [AuthorSuccess, Error])
PostResponse = strawberry.union("PostResponses", [PostSuccess, Error])
PostCommentResponse = strawberry.union("PostCommentResponses", [PostCommentSuccess, Error])

