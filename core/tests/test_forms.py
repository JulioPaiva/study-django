import pytest

from core.forms import ContactForm


@pytest.mark.django_db
def test_contact_form_valid(form_data_payload: dict):
    form = ContactForm(data=form_data_payload)

    assert form.is_valid() is True


@pytest.mark.django_db
def test_contact_form_invalid():
    form = ContactForm(data={})

    assert form.is_valid() is False
