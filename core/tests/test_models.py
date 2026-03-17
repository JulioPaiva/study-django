import pytest

from core.models import Email, Profile


@pytest.mark.django_db
def test_profile_str():
    profile = Profile.objects.create(
        name="Julio",
        bio="Backend Developer",
    )

    assert str(profile) == "Julio"


@pytest.mark.django_db
def test_email_str():
    _email = "juliopaiva.ti@gmail.com"
    profile = Profile.objects.create(
        name="Julio",
        bio="Backend Developer",
    )

    email = Email.objects.create(profile=profile, email=_email)

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
