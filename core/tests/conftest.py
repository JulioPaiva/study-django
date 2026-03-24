import pytest

from core.models import Profile


@pytest.fixture
def profile_payload() -> dict:
    return {
        "name": "Julio",
        "nickname": "Jul.io",
        "github": "https://github.com/julio",
        "instagram": "instagram",
        "linkedin": "linkedin",
        "video": "video",
        "brand": "brand",
        "bio": "bio",
        "message": "message",
        "position": "Backend Developer",
        "welcome_message": "Bem-vindo ao meu perfil!",
    }


@pytest.fixture
def profile_factory(profile_payload) -> Profile:
    return Profile.objects.create(**profile_payload)


@pytest.fixture
def form_data_payload() -> dict:
    return {
        "name": "Julio",
        "email": "juliopaiva.ti@gmail.com",
        "subject": "Teste de contato",
        "message": "Olá, este é um teste de contato.",
    }
