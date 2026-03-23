import pytest
from django.core import mail
from django.urls import reverse

from core.models import Profile


@pytest.mark.django_db
def test_index_template_used(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_index_context_contains_profile(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "profile" in response.context


@pytest.mark.django_db
def test_index_view_post_success(client):
    Profile.objects.create(name="Julio")

    url = reverse("index")
    data = {
        "name": "Julio",
        "email": "julio@dev.com",
        "subject": "Deploy",
        "message": "Mensagem de teste",
    }

    response = client.post(url, data)

    assert response.status_code == 302
    assert response.url == reverse("index")
    assert len(mail.outbox) == 1
    assert "Julio" in mail.outbox[0].body


@pytest.mark.django_db
def test_index_view_post_invalid(client):
    url = reverse("index")
    data = {"name": "Julio"}

    response = client.post(url, data)

    assert response.status_code == 200
    assert "email" in response.context["form"].errors
    assert len(mail.outbox) == 0
