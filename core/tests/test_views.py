import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_index_status_code(client):
    response = client.get("/")

    assert response.status_code == 200

@pytest.mark.django_db
def test_index_context(client):
    response = client.get("/")

    assert response.context["key"] == "Django"
