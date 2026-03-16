import pytest

from core.models import Profile


@pytest.mark.django_db
def test_profile_str():
    profile = Profile.objects.create(
        name="Julio",
        bio="Backend Developer",
    )

    assert str(profile) == "Julio"