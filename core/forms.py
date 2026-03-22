import logging

from django import forms
from django.conf import settings
from django.core.mail.message import EmailMessage
from django.template.loader import render_to_string

logger = logging.getLogger("app")


class ContactForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="Email")
    subject = forms.CharField(label="Assunto", max_length=100)
    message = forms.CharField(label="Mensagem", widget=forms.Textarea)

    def send_mail(self):
        email_contact = self.cleaned_data["email"]
        logger.info(f"Tentando enviar e-mail de: {email_contact}")

        html_content = render_to_string(
            "emails/contact.html",
            {
                "name": self.cleaned_data["name"],
                "email": email_contact,
                "subject": self.cleaned_data["subject"],
                "message": self.cleaned_data["message"],
            },
        )

        email_message = EmailMessage(
            subject=f"Contato do site: {self.cleaned_data['subject']}",
            body=html_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DEFAULT_FROM_EMAIL],
            headers={"Reply-To": email_contact},
        )

        try:
            email_message.content_subtype = "html"
            email_message.send()
            logger.info(f"E-mail enviado com sucesso de: {email_contact}")
        except Exception as e:
            logger.error(f"Erro ao enviar e-mail. Erro: {str(e)}", exc_info=True)
            raise e
