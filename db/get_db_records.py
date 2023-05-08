import requests
from util.settings import settings
from gql.gettors import get_authors, get_posts, get_post_comments
from gql.gettors import get_author_query, get_author_variables, get_post_query, get_post_variables

url = f"http://{settings.APP_HOST}:{settings.APP_PORT}/graphql"
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, json={'query': get_authors})
print(response.json())

response = requests.post(url, headers=headers, json={'query': get_posts})
print(response.json())

response = requests.post(url, headers=headers, json={'query': get_post_comments})
print(response.json())

for v in get_author_variables:
	response = requests.post(url, headers=headers, json={'query': get_author_query, 'variables': v})
	print(response.json())

for v in get_post_variables:
	response = requests.post(url, headers=headers, json={'query': get_post_query, 'variables': v})
	print(response.json())
