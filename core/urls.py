from django.urls import path

from .views import contact, profile

urlpatterns = [
    path("", profile, name="profile"),
    path("contact/", contact, name="contact"),
]
