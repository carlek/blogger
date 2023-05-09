#blogger


### FastAPI app with graphql api to support blog data 

Build:  
```
docker-compose build
```

Run:
```
docker-compose up -d
```

Populate Database:
```commandline
http://localhost:8000/docs

POST to /populate-database/
```

Query Database:
```commandline
http://localhost:8000/graphql

GraphiQL endpoint
```