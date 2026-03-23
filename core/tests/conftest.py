import pytest

from core.models import Profile


@pytest.fixture
def profile_payload() -> dict:
    return {
        "name": "Julio",
        "github": "https://github.com/julio",
        "instagram": "instagram",
        "bio": "bio",
        "position": "Backend Developer",
    }


@pytest.fixture
def profile_factory(profile_payload) -> Profile:
    return Profile.objects.create(
        name=profile_payload["name"],
        github=profile_payload["github"],
        instagram=profile_payload["instagram"],
        bio=profile_payload["bio"],
        position=profile_payload["position"],
    )


@pytest.fixture
def form_data_payload() -> dict:
    return {
        "name": "Julio",
        "email": "juliopaiva.ti@gmail.com",
        "subject": "Teste de contato",
        "message": "Olá, este é um teste de contato.",
    }
