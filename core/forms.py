import logging

from django import forms
from django.conf import settings
from django.core.mail.message import EmailMessage

logger = logging.getLogger("app")


class ContactForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="Email")
    subject = forms.CharField(label="Assunto", max_length=100)
    message = forms.CharField(label="Mensagem", widget=forms.Textarea)

    def send_mail(self):
        email_contact = self.cleaned_data["email"]
        logger.info(f"Tentando enviar e-mail de: {email_contact}")

        content = (
            f"Nome: {self.cleaned_data['name']}\n"
            f"Email: {email_contact}\n"
            f"Assunto: {self.cleaned_data['subject']}\n\n"
            f"Mensagem:\n{self.cleaned_data['message']}"
        )

        email_message = EmailMessage(
            subject=f"Contato do site: {self.cleaned_data['subject']}",
            body=content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DEFAULT_FROM_EMAIL],
            headers={"Reply-To": email_contact},
        )

        try:
            email_message.send()
            logger.debug(f"E-mail enviado com sucesso de: {email_contact}")
        except Exception as e:
            logger.error(f"Erro ao enviar e-mail. Erro: {str(e)}", exc_info=True)
            raise e
