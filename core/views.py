import logging

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from core.models import Email, Phone, Profile, Services

from .forms import ContactForm

logger = logging.getLogger("app")


class IndexView(FormView):
    template_name = "index.html"
    form_class = ContactForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        context["services"] = Services.objects.filter(profile=context["profile"])
        context["emails"] = Email.objects.filter(profile=context["profile"])
        context["phones"] = Phone.objects.filter(profile=context["profile"])

        return context

    def form_valid(self, form, *args, **kwargs):
        try:
            form.send_mail()
            messages.success(self.request, "E-mail enviado com sucesso!")
            logger.info("Fluxo de contato finalizado com sucesso.")

        except Exception as e:
            logger.error(f"Erro ao enviar e-mail. Erro: {str(e)}", exc_info=True)
            messages.error(self.request, "Erro ao enviar e-mail")
            raise e

        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        logger.warning(f"Tentativa de envio inválida: {form.errors.as_json()}")
        messages.error(self.request, "Erro ao enviar e-mail")
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


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
