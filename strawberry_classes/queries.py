import strawberry
from sqlalchemy import select
from typing import List
from strawberry_classes.models import Author, Post, PostComment
global SessionLocal

@strawberry.type
class Query:
	@strawberry.field
	def get_author(self, id: int) -> Author:
		with SessionLocal as session:
			author = session.query(Author).filter_by(id=id).first()
			return author

	@strawberry.field
	def get_post(self, id: int) -> Post:
		with SessionLocal as session:
			post = session.query(Post).filter_by(id=id).first()
			return post

	@strawberry.field
	def get_post_comment(self, id: int) -> PostComment:
		with SessionLocal as session:
			post_comment = session.query(PostComment).filter_by(id=id).first()
			return post_comment

	@strawberry.field
	async def get_authors(self) -> List[Author]:
		async with SessionLocal as session:
			authors = await session.execute(select(Author))
			return authors.scalars().all()

	@strawberry.field
	async def get_posts(self) -> List[Post]:
		async with SessionLocal as session:
			posts = await session.execute(select(Post))
			return posts.scalars().all()

	@strawberry.field
	async def get_post_comments(self) -> List[PostComment]:
		async with SessionLocal as session:
			post_comments = await session.execute(select(PostComment))
			return post_comments.scalars().all()
