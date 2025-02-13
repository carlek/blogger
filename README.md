# blogger


### FastAPI app with GraphQL API to support blog data 

*Choose one or the other, because at this time (afaik) there is no docker-compose provider for terraform to work with.*

Docker version:   
```sh
docker compose build 
docker compose up -d
docker compose down -v
```
Terraform version:   
```sh
cd terraform
terraform init
terraform plan
terraform apply
```

Populate Database with FastAPI
```
http://localhost:8000/docs

POST to /populate-database/
```

Query Database:  GraphiQL
```
http://localhost:8000/graphql
```

Run Tests: 
```
docker exec <app-container> pytest tests --asyncio-mode=strict
```

TODO:
1. Explicit, usable, resolvers
2. Authentication


Sample Queries:
```graphql
# create author
mutation CreateAuthor($username: String!, $email: String!, $password: String!) {
  createAuthor(username: $username, email: $email, password: $password) {
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
# variables 
{"username": "bigbird", "email": "big@bird.com", "password": "hithere!!!"}
```
![create author](createAuthor.png)

```graphql
# get authors
query {
  getAuthors {
    id
    username
    email
    createdAt
    updatedAt
  }
}
```
![get Authors](getAuthors.png)

**More examples:**
```graphql
# get author
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
# variables
{"id": 1}

# edit author
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
# variables
{"id": 5, "username": "new_username_5", "email": "new_email_5", "password": "new_password_5"}

# delete author
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
# variables
{"id": 1}
```
