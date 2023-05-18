
get_author_query = """
query GetAuthor($id: Int!) {
  getAuthor(id: $id) {
    __typename
    ... on AuthorSuccess {
      author {
        id
        username
        email
        createdAt
        updatedAt
      }
      message
    }
    ... on Error {
      message
    }
  }
}
"""

get_author_variables = \
	[
		{"id": 1},
		{"id": 2},
		{"id": 123123123},
	]


get_post_query = """
query GetPost($id: Int!) {
  getPost(id: $id) {
    __typename
    ... on PostSuccess {
      post {
        id
        title
        content
        createdAt
        updatedAt
      }
      message
    }
    ... on Error {
      message
    }
  }
}
"""

get_post_variables = \
  [
    {"id": 1},
    {"id": 123},
    {"id": 99},
  ]

# get_author(id: int) -> Author:
get_author = """
query {
  getAuthor(id: 1) {
    username
    email
    password
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
