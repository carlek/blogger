from datetime import datetime

import strawberry
from sqlalchemy import text, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from db.models import Author as db_Author, Post as db_Post, PostComment as db_PostComment
from strawberry_classes.models import Author, Post, PostComment
from util.settings import settings

@strawberry.type
class Mutation:
	@strawberry.mutation
	async def create_author(self, username: str, email: str, password: str) -> Author:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				create_time = datetime.now()
				db_author = db_Author(
					username=username,
					email=email,
					password=password,
					created_at=create_time,
					updated_at=create_time,
				)
				session.add(db_author)
				await session.commit()
				await session.refresh(db_author)
				return Author(
					id=db_author.id,
					username=username,
					email=email,
					password=password,
					created_at=create_time,
					updated_at=create_time
				)

	@strawberry.mutation
	async def edit_author(self, id: int, username: str = None, email: str = None, password: str = None) -> Author:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				result = await session.execute(select(db_Author).where(db_Author.id == id))
				if None is (db_author := result.fetchone()):
					raise ValueError(f"Author with id {id} not found")
				if username:
					db_author.Author.username = username
				if email:
					db_author.Author.email = email
				if password:
					db_author.Author.password = password
				db_author.Author.updated_at = datetime.now()
				author = Author(
						username=db_author.Author.username,
						email=db_author.Author.email,
						password=db_author.Author.password,
						created_at=db_author.Author.created_at,
						updated_at=db_author.Author.updated_at,
					)
				await session.commit()
				return author

	@strawberry.mutation
	async def delete_author(self, id: int) -> bool:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				db_author = await session.get(db_Author, id)
				if not db_author:
					raise ValueError(f"Author with id {id} not found")
				session.delete(db_author)
				await session.commit()
				return True

	@strawberry.mutation
	async def create_post(
			self, title: str, content: str, author_id: int
	) -> Post:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				db_post = db_Post(
					title=title,
					content=content,
					author_id=author_id,
					created_at=datetime.now(),
					updated_at=datetime.now(),
				)
				session.add(db_post)
				await session.commit()
				await session.refresh(db_post)
				return Post(
					id=db_post.id,
					title=title,
					content=content,
					author_id=author_id,
					created_at=datetime.now(),
					updated_at=datetime.now(),
				)

	@strawberry.mutation
	async def create_post_comment(self, post_id: int, author_id: int, content: str) -> PostComment:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				db_post_comment = db_PostComment(
					post_id=post_id,
					author_id=author_id,
					content=content,
					created_at=datetime.now(),
					updated_at=datetime.now(),
				)
				session.add(db_post_comment)
				await session.commit()
				await session.refresh(db_post_comment)
				return PostComment(
					id=db_post_comment.id,
					post_id=post_id,
					author_id=author_id,
					content=content,
					created_at=datetime.now(),
					updated_at=datetime.now(),
				)

	@strawberry.mutation
	async def truncate_table(self, table_name: str) -> str:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				await session.execute(text(f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE;"))
				await session.commit()
				return "success"
