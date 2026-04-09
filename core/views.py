import logging

from django.contrib import messages
from django.shortcuts import redirect

# from django.urls import reverse_lazy
from django.views.generic import TemplateView

from core.models import Profile

from .forms import ContactForm, NewsletterForm

logger = logging.getLogger("app")


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context["contact_form"] = kwargs.get("contact_form", ContactForm())
        context["newsletter_form"] = kwargs.get("newsletter_form", NewsletterForm())

        context["profile"] = Profile.objects.prefetch_related(
            "services", "emails", "phones", "skills", "posts"
        ).first()

        return context

    def post(self, request, *args, **kwargs):
        if "contact_form" in request.POST:
            contact_form = ContactForm(request.POST)
            newsletter_form = NewsletterForm()

            if contact_form.is_valid():
                try:
                    contact_form.send_mail()
                    messages.success(self.request, "E-mail enviado com sucesso!")
                    logger.info("Fluxo de contato finalizado com sucesso.")
                except Exception as e:
                    logger.error(
                        f"Erro ao enviar e-mail. Erro: {str(e)}", exc_info=True
                    )
                    messages.error(self.request, "Erro ao enviar e-mail")
                    raise

            return self.render_to_response(
                self.get_context_data(
                    contact_form=ContactForm(), newsletter_form=newsletter_form
                )
            )

        elif "newsletter_form" in request.POST:
            newsletter_form = NewsletterForm(request.POST)
            contact_form = ContactForm()
            if newsletter_form.is_valid():
                newsletter_form.save()
                messages.success(
                    request, "Inscrição na newsletter realizada com sucesso!"
                )
                logger.info(
                    "Nova inscrição na newsletter: %s",
                    newsletter_form.cleaned_data["email"],
                )

                return redirect("index")

            return self.render_to_response(
                self.get_context_data(
                    contact_form=contact_form, newsletter_form=NewsletterForm()
                )
            )

        else:
            logger.warning("Erro ao encontrar o formulário.")
            messages.error(request, "Erro ao enviar formulário")
            return redirect("index")


class NotFoundView(TemplateView):
    template_name = "404.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=404)


class ServerErrorView(TemplateView):
    template_name = "500.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=500)
