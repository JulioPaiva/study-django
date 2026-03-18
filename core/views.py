from django.contrib import messages
from django.shortcuts import render

from core.models import Profile

from .forms import ContactForm


def index(request):
    profiles = Profile.objects.all()

    context = {
        "key": profiles,
    }
    return render(request, "index.html", context)


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
