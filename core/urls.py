from django.urls import path

from .views import IndexView, NotFoundView, ServerErrorView

handler404 = NotFoundView.as_view()
handler500 = ServerErrorView.as_view()

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
