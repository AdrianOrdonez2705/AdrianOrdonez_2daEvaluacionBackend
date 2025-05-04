import pytest
from django.test import RequestFactory

@pytest.fixture
def rf():
    return RequestFactory()

@pytest.fixture
def graphql_query(rf):
    def func(query: str):
        request = rf.post('/graphql/', {'query': query})
        return request
    return func