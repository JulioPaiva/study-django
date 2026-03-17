from django.urls import path

from .views import contact, index

urlpatterns = [
    path("", index),
    path("contact/", contact, name="contact"),
]
