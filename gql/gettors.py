
get_author_query = """
query GetAuthor($id: Int!) {
  getAuthor(id: $id) {
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
    id
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
