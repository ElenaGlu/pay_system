import json

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_get_item(client, item):
    url = reverse('get_item')
    data = {
            "id": 1
        }
    response = client.get(url, data)
    # resp_json = response.json()
    assert response.status_code == 200
    # assert resp_json == [
    #     {
    #         'description': 'size:1500',
    #         'id': 2,
    #         'price': '1999.00',
    #         'quantity': 10,
    #         'store_name_id': 2,
    #         'title_product': 'computer table',
    #         'active_status': True
    #     }
    # ]