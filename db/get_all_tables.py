import requests
from util.settings import settings
from gql.gettors import get_authors, get_posts, get_post_comments

url = f"http://{settings.APP_HOST}:{settings.APP_PORT}/graphql"
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, json={'query': get_authors})
print(response.json())

response = requests.post(url, headers=headers, json={'query': get_posts})
print(response.json())

response = requests.post(url, headers=headers, json={'query': get_post_comments})
print(response.json())

