from django.urls import include, path

from .views import IndexView, NotFoundView, ServerErrorView

handler404 = NotFoundView.as_view()
handler500 = ServerErrorView.as_view()

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('i18n/', include('django.conf.urls.i18n')),
]
