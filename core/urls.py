from django.urls import path

from .views import contact, profile, recommendation

urlpatterns = [
    path("", profile, name="profile"),
    path("contact/", contact, name="contact"),
    path("recommendation/", recommendation, name="recommendation"),
]
