from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Profile, Recommendation

from .forms import ContactForm


class IndexView(TemplateView):
    template_name = "index.html"

def profile(request):
    profiles = Profile.objects.all()

    context = {
        "key": profiles,
    }
    return render(request, "profile.html", context)


def contact(request):
    form = ContactForm(request.POST or None)

    if str(request.method).upper() == "POST":
        if form.is_valid():
            form.send_mail()
            messages.success(request, "Mensagem enviada com sucesso!")
            form = ContactForm()
        else:
            messages.error(
                request,
                "Formulário inválido. Por favor, corrija os erros e tente novamente.",  # NOQA
            )

    context = {
        "form": form,
    }

    return render(request, "contact.html", context)


def recommendation(request):
    recommendations = Recommendation.objects.all()

    context = {
        "recommendations": recommendations,
    }

    return render(request, "recommendation.html", context)
