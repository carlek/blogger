from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

# SQLAlchemy models
class Author(Base):
	__tablename__ = "author"
	id = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(String, unique=True)
	email = Column(String, unique=True)
	password = Column(String)
	created_at = Column(DateTime, default=datetime.utcnow)
	updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
	posts = relationship("Post", back_populates="author", cascade="all, delete")
	comments = relationship("PostComment", back_populates="author", cascade="all, delete")


class Post(Base):
	__tablename__ = "post"
	id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(String)
	content = Column(String)
	author_id = Column(Integer, ForeignKey("author.id"))
	created_at = Column(DateTime, default=datetime.utcnow)
	updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
	author = relationship("Author", back_populates="posts", cascade="all, delete")
	comments = relationship("PostComment", back_populates="post", cascade="all, delete")


class PostComment(Base):
	__tablename__ = "postcomment"
	id = Column(Integer, primary_key=True, autoincrement=True)
	post_id = Column(Integer, ForeignKey("post.id"))
	author_id = Column(Integer, ForeignKey("author.id"))
	content = Column(String)
	created_at = Column(DateTime, default=datetime.utcnow)
	updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
	post = relationship("Post", back_populates="comments")
	author = relationship("Author", back_populates="comments")
