edit_author_query = '''
mutation EditAuthor($id: Int!, $username: String, $email: String, $password: String) {
  editAuthor(id: $id, username: $username, email: $email, password: $password) {
    ... on AuthorSuccess {
      author {
        username
        email
        password
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
'''

edit_author_variables = \
	[
		{'id': 1, 'password': 'new_password_1'},
		{'id': 2, 'username': 'new_username_2'},
		{'id': 3, 'email': 'new_email_3'},
		{'id': 4, 'username': 'new_username_4', 'password': 'new_password_4'},
		{'id': 5, 'username': 'new_username_5', 'email': 'new_email_5', 'password': 'new_password_5'},
	]

delete_author_query = '''
mutation DeleteAuthor($id: Int!) {
  deleteAuthor(id: $id) {
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
'''

delete_author_variables = \
	[
		{'id': 1},
	]

delete_post_query = \
'''
mutation DeletePost($id: Int!) {
  deletePost(id: $id) {
    ... on PostSuccess {
      post {
        id
        title
        content
        authorId
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
'''
