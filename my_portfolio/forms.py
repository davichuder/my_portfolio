from django import forms
from django.conf import settings
from django.core.mail import EmailMessage, get_connection


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, label="Nombre")
    email = forms.EmailField(label="Email")
    inquiry = forms.CharField(max_length=70, label="Asunto")
    message = forms.CharField(widget=forms.Textarea, label="Mensaje")

    def get_info(self):
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('inquiry')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):
        subject, msg = self.get_info()

        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]
            EmailMessage(subject, msg, email_from, recipient_list, connection=connection).send()
