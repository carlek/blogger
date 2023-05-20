from datetime import datetime
import strawberry
from sqlalchemy import text, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.exc import IntegrityError

from db.models import Author as db_Author, Post as db_Post, PostComment as db_PostComment
from strawberry_classes.models import Author, Post, PostComment
from strawberry_classes.models import AuthorSuccess, AuthorResponse, Error
from strawberry_classes.models import PostSuccess, PostResponse
from strawberry_classes.models import PostCommentSuccess, PostCommentResponse
from util.settings import settings

@strawberry.type
class Mutations:
	@strawberry.mutation
	async def create_author(self, username: str, email: str, password: str) -> AuthorResponse:
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
				try:
					session.add(db_author)
					await session.commit()
					await session.refresh(db_author)
					return AuthorSuccess(author=db_author, message="Author created")
				except IntegrityError as e:
					return Error(message=f"Cannot create author: {e}")

	@strawberry.mutation
	async def edit_author(self, id: int, username: str = None, email: str = None, password: str = None) -> AuthorResponse:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				result = await session.execute(select(db_Author).where(db_Author.id == id))
				if None is (db_author := result.fetchone()):
					return Error(message=f"Author not found, not edited: id = {id}")
				if username:
					db_author.Author.username = username
				if email:
					db_author.Author.email = email
				if password:
					db_author.Author.password = password
				db_author.Author.updated_at = datetime.now()
				author = Author(
					id=db_author.Author.id,
					username=db_author.Author.username,
					email=db_author.Author.email,
					password=db_author.Author.password,
					created_at=db_author.Author.created_at,
					updated_at=db_author.Author.updated_at,
				)
				try:
					await session.commit()
					return AuthorSuccess(author=author, message="Author updated")
				except Exception as e:
					return Error(message=f"Author not found, not edited: id={id} error={e}")

	@strawberry.mutation
	async def delete_author(self, id: int) -> AuthorResponse:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				db_author = await session.get(db_Author, id)
				if not db_author:
					return Error(message=f"Author not found, not deleted: id={id}")
				try:
					await session.delete(db_author)
					await session.commit()
					return AuthorSuccess(author=db_author, message="Author deleted successfully")
				except Exception as e:
					return Error(message=f"Author not deleted: {e}")

	@strawberry.mutation
	async def create_post(self, title: str, content: str, author_id: int) -> PostResponse:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				create_time = datetime.now()
				db_post = db_Post(
					title=title,
					content=content,
					author_id=author_id,
					created_at=create_time,
					updated_at=create_time,
				)
				try:
					session.add(db_post)
					await session.commit()
					await session.refresh(db_post)
					return PostSuccess(post=db_post, message="Post created")
				except IntegrityError as e:
					return Error(message=f"Cannot create post: {e}")

	@strawberry.mutation
	async def edit_post(self, id: int, title: str, content: str) -> PostResponse:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				result = await session.execute(select(db_Post).where(db_Post.id == id))
				if None is (db_post := result.fetchone()):
					return Error(message=f"Post not found, not edited: id = {id}")
				if title:
					db_post.Post.title = title
				if content:
					db_post.Post.content = content
				db_post.Post.updated_at = datetime.now()
				post = Post(
					id=db_post.Post.id,
					title=db_post.Post.title,
					content=db_post.Post.content,
					author_id=db_post.Post.author_id,
					created_at=db_post.Post.created_at,
					updated_at=db_post.Post.updated_at,
				)
				try:
					await session.commit()
					return PostSuccess(post=post, message="Post updated")
				except Exception as e:
					return Error(message=f"Post not found, not edited: id={id} error={e}")

	@strawberry.mutation
	async def delete_post(self, id: int) -> PostResponse:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				db_post = await session.get(db_Post, id)
				if not db_post:
					return Error(message=f"Post not found, not deleted: id={id}")
				try:
					await session.delete(db_post)
					await session.commit()
					return PostSuccess(post=db_post, message="Post deleted successfully")
				except Exception as e:
					return Error(message=f"Post not deleted: {e}")

	@strawberry.mutation
	async def create_post_comment(self, post_id: int, author_id: int, content: str) -> PostCommentResponse:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				create_time = datetime.now()
				db_post_comment = db_PostComment(
					post_id=post_id,
					author_id=author_id,
					content=content,
					created_at=create_time,
					updated_at=create_time,
				)
				try:
					session.add(db_post_comment)
					await session.commit()
					await session.refresh(db_post_comment)
					return PostCommentSuccess(postcomment=db_post_comment, message="PostComment created")
				except IntegrityError as e:
					return Error(message=f"Cannot create PostComment: {e}")

	@strawberry.mutation
	async def edit_post_comment(self, id: int, content: str) -> PostCommentResponse:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				result = await session.execute(select(db_PostComment).where(db_PostComment.id == id))
				if None is (db_post_comment := result.fetchone()):
					return Error(message=f"PostComment not found, not edited: id = {id}")
				if content:
					db_post_comment.PostComment.content = content
				db_post_comment.PostComment.updated_at = datetime.now()
				post_comment = PostComment(
					id=db_post_comment.PostComment.id,
					post_id=db_post_comment.PostComment.post_id,
					author_id=db_post_comment.PostComment.author_id,
					content=db_post_comment.PostComment.content,
					created_at=db_post_comment.PostComment.created_at,
					updated_at=db_post_comment.PostComment.updated_at,
				)
				try:
					await session.commit()
					return PostCommentSuccess(postcomment=post_comment, message="PostComment updated")
				except Exception as e:
					return Error(message=f"PostComment not found, not edited: id={id} error={e}")

	@strawberry.mutation
	async def delete_post_comment(self, id: int) -> PostCommentResponse:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				db_post_comment = await session.get(db_PostComment, id)
				if not db_post_comment:
					return Error(message=f"PostComment not found, not deleted: id={id}")
				try:
					await session.delete(db_post_comment)
					await session.commit()
					return PostCommentSuccess(postcomment=db_post_comment, message="PostComment deleted successfully")
				except Exception as e:
					return Error(message=f"PostComment not deleted: {e}")

	@strawberry.mutation
	async def truncate_table(self, table_name: str) -> str:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				await session.execute(text(f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE;"))
				await session.commit()
				return "success"
