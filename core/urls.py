from django.urls import path

from .views import contact, profile, recommendation, IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("profile/", profile, name="profile"),
    path("contact/", contact, name="contact"),
    path("recommendation/", recommendation, name="recommendation"),
]
