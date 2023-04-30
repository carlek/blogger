import strawberry
from strawberry_classes.models import Author, Post, PostComment
from datetime import datetime

global SessionLocal

@strawberry.type
class Mutation:
	@strawberry.mutation
	async def create_author(self, username: str, email: str, password: str) -> Author:
		async with SessionLocal as session:
			author = Author(
				username=username,
				email=email,
				password=password,
				created_at=datetime.now(),
				updated_at=datetime.now(),
			)
			session.add(author)
			await session.commit()
			return author

	@strawberry.mutation
	async def create_post(
			self, title: str, content: str, author_id: int
	) -> Post:
		async with SessionLocal as session:
			post = Post(
				title=title,
				content=content,
				author_id=author_id,
				created_at=datetime.now(),
				updated_at=datetime.now(),
			)
			session.add(post)
			await session.commit()
			return post

	@strawberry.mutation
	async def create_post_comment(self, post_id: int, author_id: int, content: str) -> PostComment:
		async with SessionLocal as session:
			post_comment = PostComment(
				post_id=post_id,
				author_id=author_id,
				content=content,
				created_at=datetime.now(),
				updated_at=datetime.now(),
			)
			session.add(post_comment)
			await session.commit()
			return post_comment