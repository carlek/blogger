import strawberry
from sqlalchemy import select
from typing import List
from strawberry_classes.models import Author, Post, PostComment
from strawberry_classes.models import AuthorSuccess, AuthorResponse
from strawberry_classes.models import PostSuccess, PostResponse
from strawberry_classes.models import PostCommentSuccess, PostCommentResponse
from strawberry_classes.models import Error
from db.models import Author as db_Author, Post as db_Post, PostComment as db_PostComment
from util.settings import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

@strawberry.type
class Queries:

	@strawberry.field
	async def get_author(self, id: int) -> AuthorResponse:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				result = await session.execute(select(db_Author).where(db_Author.id == id))
				if None is (db_author := result.fetchone()):
					return Error(message=f"Author with id={id} not found")
				author = Author(
					id=db_author.Author.id,
					username=db_author.Author.username,
					email=db_author.Author.email,
					password=db_author.Author.password,
					created_at=db_author.Author.created_at,
					updated_at=db_author.Author.updated_at,
				)
				return AuthorSuccess(
					author=author,
					message=f"Author with id={id} found"
				)

	@strawberry.field
	async def get_post(self, id: int) -> PostResponse:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				result = await session.execute(select(db_Post).where(db_Post.id == id))
				if None is (db_post := result.fetchone()):
					return Error(message=f"Post with id {id} not found")
				post = Post(
					id=db_post.Post.id,
					title=db_post.Post.title,
					content=db_post.Post.content,
					author_id=db_post.Post.author_id,
					created_at=db_post.Post.created_at,
					updated_at=db_post.Post.updated_at,
				)
				return PostSuccess(
					post=post,
					message=f"Post with id={id} found"
				)

	@strawberry.field
	async def get_post_comment(self, id: int) -> PostCommentResponse:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				result = await session.execute(select(db_PostComment).where(db_PostComment.id == id))
				if None is (db_post_comment := result.fetchone()):
					return Error(message=f"PostComment with id {id} not found")
				post_comment = PostComment(
					id=db_post_comment.PostComment.id,
					post_id=db_post_comment.PostComment.post_id,
					author_id=db_post_comment.PostComment.author_id,
					content=db_post_comment.PostComment.content,
					created_at=db_post_comment.PostComment.created_at,
					updated_at=db_post_comment.PostComment.updated_at,
				)
				return PostCommentSuccess(
					postcomment=post_comment,
					message=f"PostComment with id={id} found"
				)

	@strawberry.field
	async def get_authors(self) -> List[Author]:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				result = await session.execute(select(db_Author))
				db_authors = result.all()
				return [
					Author(
						id=d.Author.id,
						username=d.Author.username,
						email=d.Author.email,
						password=d.Author.password,
						created_at=d.Author.created_at,
						updated_at=d.Author.updated_at,
					)
					for d in db_authors
				]

	@strawberry.field
	async def get_posts(self) -> List[Post]:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				result = await session.execute(select(db_Post))
				db_posts = result.all()
				return [
					Post(
						id=d.Post.id,
						title=d.Post.title,
						content=d.Post.content,
						author_id=d.Post.author_id,
						created_at=d.Post.created_at,
						updated_at=d.Post.updated_at,
					)
					for d in db_posts
				]

	@strawberry.field
	async def get_post_comments(self) -> List[PostComment]:
		async with create_async_engine(url=settings.DB_CONNECTION_STR, echo=True).begin() as conn:
			async with AsyncSession(bind=conn) as session:
				result = await session.execute(select(db_PostComment))
				db_post_comments = result.all()
				return [
					PostComment(
						id=d.PostComment.id,
						post_id=d.PostComment.post_id,
						author_id=d.PostComment.author_id,
						content=d.PostComment.content,
						created_at=d.PostComment.created_at,
						updated_at=d.PostComment.updated_at,
					)
					for d in db_post_comments
				]

@strawberry.type
class Query:
	getAuthor: AuthorResponse = strawberry.field(resolver=Queries.get_author)
	getPost: PostResponse = strawberry.field(resolver=Queries.get_post)
	getPostComment: PostCommentResponse = strawberry.field(resolver=Queries.get_post_comment)
	getAuthors: List[Author] = strawberry.field(resolver=Queries.get_authors)
	getPosts: List[Post] = strawberry.field(resolver=Queries.get_posts)
	getPostComments: List[PostComment] = strawberry.field(resolver=Queries.get_post_comments)
