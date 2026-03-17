from django.shortcuts import render
from django.contrib import messages 

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
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            print(
                f"Nome: {name}",
                f"Email: {email}",
                f"Assunto: {subject}",
                f"Mensagem: {message}",
                sep="\n",
            )

            messages.success(request, "Mensagem enviada com sucesso!")
        else:
            messages.error(
                request,
                "Formulário inválido. Por favor, corrija os erros e tente novamente." # NOQA
            )

    context = {
        "form": form,
    }

    return render(request, "contact.html", context)
