import pytest
import requests
from util.settings import settings
from gql.utils import truncate_table_query, truncate_table_variables

@pytest.fixture
def url() -> str:
	return f"http://{settings.APP_HOST}:{settings.APP_PORT}/graphql"

@pytest.fixture
def headers() -> dict:
	return {'Content-Type': 'application/json'}

@pytest.fixture
def clear_tables(url, headers) -> None:
	for v in truncate_table_variables:
		response = requests.post(url=url, headers=headers, json={'query': truncate_table_query, 'variables': v})
		assert response
