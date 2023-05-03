import requests
from util.settings import settings
from gql.creators import create_author_query, create_author_variables, create_post_comment_query
from gql.creators import create_post_query, create_post_variables, create_post_comment_variables
from gql.utils import truncate_table_query, truncate_table_variables

url = f"http://{settings.APP_HOST}:{settings.APP_PORT}/graphql"
headers = {'Content-Type': 'application/json'}

query = truncate_table_query
for v in truncate_table_variables:
    response = requests.post(url, headers=headers, json={'query': query, 'variables': v})
    print(response.json())

query = create_author_query
for v in create_author_variables:
    response = requests.post(url, headers=headers, json={'query': query, 'variables': v})
    print(response.json())

query = create_post_query
for v in create_post_variables:
    response = requests.post(url, headers=headers, json={'query': query, 'variables': v})
    print(response.json())

query = create_post_comment_query
for v in create_post_comment_variables:
    response = requests.post(url, headers=headers, json={'query': query, 'variables': v})
    print(response.json())