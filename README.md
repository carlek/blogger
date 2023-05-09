# blogger


### FastAPI app with graphql api to support blog data 

Build:  
```
docker-compose build
```

Run:
```
docker-compose up -d
```

Populate Database: FastAPI 
```
http://localhost:8000/docs

POST to /populate-database/
```

Query Database:  GraphiQL
```
http://localhost:8000/graphql
```

Sample Queries:
```
# get authors
query {
  getAuthors {
    username
    email
    createdAt
    updatedAt
  }
}

# get author
query GetAuthor($id: Int!) {
    getAuthor(id: $id) {
        username
        email
        createdAt
    }
}
variables = {"id": 1}

# edit author
mutation EditAuthor($id: Int!, $username: String, $email: String, $password: String) {
  editAuthor(id: $id, username: $username, email: $email, password: $password) {
    username
    email
    password
    createdAt
    updatedAt
  }
}
variables = {'id': 1, 'password': 'new_password_1'}
  
```
