import strawberry
from datetime import datetime

@strawberry.type
class Author:
	username: str
	email: str
	password: str
	created_at: datetime
	updated_at: datetime

@strawberry.type
class Post:
	title: str
	content: str
	author_id: int
	created_at: datetime
	updated_at: datetime

@strawberry.type
class PostComment:
	post_id: int
	author_id: int
	content: str
	created_at: datetime
	updated_at: datetime
