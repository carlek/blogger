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
class Error:
	message: str
