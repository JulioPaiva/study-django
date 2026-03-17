from django.shortcuts import render

from core.models import Profile


def index(request):
    profiles = Profile.objects.all()

    context = {
        "key": profiles,
    }
    return render(request, "index.html", context)
