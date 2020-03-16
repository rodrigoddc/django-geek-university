from django import forms
from django.core.mail.message import EmailMessage
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    """
    Form class for sending emails from index page to contac/suport
    of the plataform
    """
    name = forms.CharField(label=_('Name'), max_length=100)
    email = forms.EmailField(label=_('Email'), max_length=100)
    subject = forms.CharField(label=_('Subject'), max_length=100)
    message = forms.CharField(label=_('Message'), widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        mail = EmailMessage(
            subject=subject,
            body=message,
            from_email=email,
            to=['contact@mydomain.com', ],
            headers={'Replay-to': name}
        )
        mail.send()
