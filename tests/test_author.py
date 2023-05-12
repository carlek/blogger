import pytest
from strawberry_classes.queries import Query

query = Query()

@pytest.mark.asyncio
async def test_get_author():
    result = await query.get_author(1)
    assert result.username == "johndoe"
    assert result.email == "johndoe@example.com"
    assert result.password == "password123"
