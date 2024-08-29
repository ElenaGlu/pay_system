import pytest

from app import models


@pytest.fixture()
def item():
    items = [
        {
            "id": 1,
            "name": "test1",
            "description": "test1",
            "price": 100.00,
        },
        {
            "id": 2,
            "name": "test2",
            "description": "test2",
            "price": 200.45,
        },
        {
            "id": 3,
            "name": "test3",
            "description": "test3",
            "price": 300.01,
        },
    ]
    temporary = []
    for obj in items:
        temporary.append(models.Item(**obj))
    return models.Item.objects.bulk_create(temporary)
