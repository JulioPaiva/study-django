import pytest

from core.models import Base, Email, Profile


@pytest.mark.django_db
def test_profile_creation(profile_payload: dict, profile_factory: Profile):
    assert str(profile_factory) is not None
    assert isinstance(profile_factory, Base)
    assert profile_factory.name == profile_payload["name"]
    assert profile_factory.github == profile_payload["github"]
    assert profile_factory.instagram == profile_payload["instagram"]
    assert profile_factory.bio == profile_payload["bio"]
    assert profile_factory.position == profile_payload["position"]
    assert profile_factory.created_at is not None
    assert profile_factory.updated_at is not None
    assert profile_factory.active is True
    assert str(profile_factory) == (
        f"{profile_payload['name']}, "
        f"{profile_payload['github']}, "
        f"{profile_payload['instagram']}, "
        f"{profile_payload['bio']}, "
        f"{profile_payload['position']}"
    )


@pytest.mark.django_db
def test_email_creation(profile_factory: Profile):
    _email = "juliopaiva.ti@gmail.com"
    email = Email.objects.create(profile=profile_factory, email=_email)

    assert str(email) == _email


@pytest.mark.django_db
def test_profile_with_multiple_emails():
    profile = Profile.objects.create(
        name="Julio",
        bio="Backend Developer",
    )

    Email.objects.create(profile=profile, email="amado.amoroso@email.com")
    Email.objects.create(profile=profile, email="funky.monkey@dominio.com")

    assert profile.emails.count() == 2
