from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, backref
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
	posts = relationship("Post", backref="author", cascade="all, delete")
	postcomments = relationship("PostComment", backref="author", cascade="all, delete")


class Post(Base):
	__tablename__ = "post"
	id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(String)
	content = Column(String)
	author_id = Column(Integer, ForeignKey("author.id", ondelete="CASCADE"))
	created_at = Column(DateTime, default=datetime.utcnow)
	updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
	postcomments = relationship("PostComment", backref="post", cascade="all, delete")


class PostComment(Base):
	__tablename__ = "postcomment"
	id = Column(Integer, primary_key=True, autoincrement=True)
	post_id = Column(Integer, ForeignKey("post.id", ondelete="CASCADE"))
	author_id = Column(Integer, ForeignKey("author.id", ondelete="CASCADE"))
	content = Column(String)
	created_at = Column(DateTime, default=datetime.utcnow)
	updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
