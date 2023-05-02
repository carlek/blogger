import strawberry
from strawberry_classes.models import Author, Post, PostComment
from db.models import Author as db_Author, Post as db_Post, PostComment as db_PostComment
from datetime import datetime
from util.settings import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

@strawberry.type
class Mutation:
	@strawberry.mutation
	async def create_author(self, username: str, email: str, password: str) -> Author:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				db_author = db_Author(
					username=username,
					email=email,
					password=password,
					created_at=datetime.now(),
					updated_at=datetime.now(),
				)
				session.add(db_author)
				await session.commit()
				return Author(
					username=username,
					email=email,
					password=password,
					created_at=datetime.now(),
					updated_at=datetime.now(),
				)

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
				return Post(
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
				return PostComment(
					post_id=post_id,
					author_id=author_id,
					content=content,
					created_at=datetime.now(),
					updated_at=datetime.now(),
				)
