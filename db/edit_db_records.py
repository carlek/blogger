import requests
from util.settings import settings
from gql.editors import edit_author_query, edit_author_variables

url = f"http://{settings.APP_HOST}:{settings.APP_PORT}/graphql"
headers = {'Content-Type': 'application/json'}

query = edit_author_query
for v in edit_author_variables:
    response = requests.post(url, headers=headers, json={'query': query, 'variables': v})
    print(response.json())
