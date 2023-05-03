# get_author(id: int) -> Author:
get_author = """
query {
  getAuthor(id: 1) {
    username
    email
    createdAt
    updatedAt
  }
}
"""

# get_post(id: int) -> Post:
get_post = """
query {
  getPost(id: 1) {
    title
    content
    authorId
    createdAt
    updatedAt
  }
}
"""

# get_post_comment(id: int) -> PostComment:
get_post_comment = """
query {
  getPostComment(id: 1) {
    postId
    authorId
    content
    createdAt
    updatedAt
  }
}
"""

# get_authors() -> List[Author]:
get_authors = """
query {
  getAuthors {
    username
    email
    createdAt
    updatedAt
  }
}
"""

# get_posts() -> List[Post]:
get_posts = """
query {
  getPosts {
    title
    content
    authorId
    createdAt
    updatedAt
  }
}
"""

# get_post_comments() -> List[PostComment]:
get_post_comments = """
query {
  getPostComments {
    postId
    authorId
    content
    createdAt
    updatedAt
  }
}
"""
