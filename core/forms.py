from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="Email")
    subject = forms.CharField(label="Assunto", max_length=100)
    message = forms.CharField(label="Mensagem", widget=forms.Textarea)

    def send_mail(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        subject = self.cleaned_data["subject"]
        message = self.cleaned_data["message"]

        email_message = EmailMessage(
            subject=subject,
            body=f"Nome: {name}\nEmail: {email}\n\n{message}",
            from_email="contato@seudominio.com.br",
            to=["contato@seudominio.com.br"],
            headers={"Reply-To": email},
        )

        email_message.send()
