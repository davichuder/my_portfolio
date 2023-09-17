from django import forms
from django.conf import settings
from django.core.mail import EmailMessage, get_connection


class ContactForm(forms.Form):
    name = forms.CharField(max_length=128, label="Nombre")
    email = forms.EmailField(max_length=128, label="Email")
    subject = forms.CharField(max_length=128, label="Asunto")
    message = forms.CharField(widget=forms.Textarea, label="Mensaje")

    def get_info(self):
        clear_data = super().clean()

        name = clear_data.get('name').strip()
        email = clear_data.get('email')
        subject = clear_data.get('subject')

        msg = f'{name} with email {email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += clear_data.get('message')

        return email, subject, msg

    def send(self):
        cc_email, subject, msg = self.get_info()

        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER]
            cc_list = [cc_email]
            EmailMessage(subject, msg, from_email, recipient_list, connection=connection, cc=cc_list).send()
