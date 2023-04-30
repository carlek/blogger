create_author = '''
mutation {
  createAuthor(
    username: "johndoe"
    email: "johndoe@example.com"
    password: "password123"
  ) {
    id
    username
    email
    createdAt
  }
}
'''

create_post = '''
mutation {
  createPost(
    title: "My First Post"
    content: "This is the content of my first post"
    authorId: 1
  ) {
    id
    title
    content
    authorId
    createdAt
  }
}
'''

create_postcomment = '''
mutation {
  createPostComment(
    postId: 1
    authorId: 1
    content: "This is my comment on the first post"
  ) {
    id
    postId
    authorId
    content
    createdAt
  }
}
'''
