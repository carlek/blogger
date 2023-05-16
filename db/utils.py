import requests
from sqlalchemy_utils import database_exists, create_database

from gql.creators import create_author_query, create_author_variables, create_post_comment_query
from gql.creators import create_post_query, create_post_variables, create_post_comment_variables
from gql.utils import truncate_table_query, truncate_table_variables
from util.settings import settings

url = f"http://{settings.APP_HOST}:{settings.APP_PORT}/graphql"
headers = {'Content-Type': 'application/json'}

def create_fresh_database():
	db_url = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}" + \
			 f"@{settings.DB_SERVER}:{settings.DB_PORT}/{settings.DB_NAME}"
	if not database_exists(db_url):
		create_database(db_url)


def truncate_tables(debug: bool = False):
		query = truncate_table_query
		for v in truncate_table_variables:
			response = requests.post(url, headers=headers, json={'query': query, 'variables': v})
			if debug: print(response.json())

def create_data(truncate: bool = True, debug: bool = False):

	if truncate:
		truncate_tables()

	query = create_author_query
	for v in create_author_variables:
		response = requests.post(url, headers=headers, json={'query': query, 'variables': v})
		if debug: print(response.json())

	query = create_post_query
	for v in create_post_variables:
		response = requests.post(url, headers=headers, json={'query': query, 'variables': v})
		if debug: print(response.json())

	query = create_post_comment_query
	for v in create_post_comment_variables:
		response = requests.post(url, headers=headers, json={'query': query, 'variables': v})
		if debug: print(response.json())
