import random

create_author_query = """
    mutation CreateAuthor($username: String!, $email: String!, $password: String!) {
        createAuthor(username: $username, email: $email, password: $password) {
            username
            email
            password
            createdAt
            updatedAt
        }
    }
"""

create_author_variables = \
	[
		{"username": "johndoe", "email": "johndoe@example.com", "password": "password123"},
		{"username": "janedoe", "email": "janedoe@example.com", "password": "password456"},
		{"username": "benfranklin", "email": "ben@franklin.com", "password": "electric123"},
		{"username": "rosieparks", "email": "rosie@parks.com", "password": "seat001"},
		{"username": "kermit", "email": "kermit@frog.com", "password": "ribbit"},
	]

create_post_query = """
    mutation CreatePost($title: String!, $content: String!, $authorId: Int!) {
        createPost(title: $title, content: $content, authorId: $authorId) {
            title
            content
            authorId
            createdAt
        }
    }
"""

create_post_variables = []
number_of_authors = len(create_author_variables)
number_of_posts = 100 // number_of_authors
for i in range(1, 1 + number_of_authors):
	for j in range(1, 1 + number_of_posts):
		v = {"title": f"Title: Post #{j} by author:{i}", "content": f"this is #{j} -author:{i}", "authorId": i}
		create_post_variables.append(v)

create_post_comment_query = """
    mutation CreatePostComment($postId: Int!, $authorId: Int!, $content: String!) {
        createPostComment(postId: $postId, authorId: $authorId, content: $content) {
            postId
            authorId
            content
            createdAt
        }
    }
"""

create_post_comment_variables = []
number_of_comments = 30
random.seed(42)
for i in range(number_of_comments):
	postnum = random.randint(1, number_of_posts)
	authornum = random.randint(1, number_of_authors)
	v = {"postId": postnum, "authorId": authornum, "content": f"Comment from author:{authornum} on post:{postnum}"}
	create_post_comment_variables.append(v)

# raw queries
create_author_raw = '''
mutation {
  createAuthor(
    username: "johndoe"
    email: "johndoe@example.com"
    password: "password123"
  ) {
    username
    email
    createdAt
  }
}
'''
create_post_raw = '''
mutation {
  createPost(
    title: "My First Post"
    content: "This is the content of my first post"
    authorId: 1
  ) {
    title
    content
    authorId
    createdAt
  }
}
'''
create_post_comment_raw = '''
mutation {
  createPostComment(
    postId: 1
    authorId: 1
    content: "This is my comment on the first post"
  ) {
    postId
    authorId
    content
    createdAt
  }
}
'''
