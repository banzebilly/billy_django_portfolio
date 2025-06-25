from django import forms
from .models import Contact
from django.core.exceptions import ValidationError
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r"^[A-Za-z\s'-]+$", name):
            raise ValidationError("Name can only contain letters, spaces, apostrophes, and hyphens.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        domain = email.split('@')[-1]
        if not domain.endswith('.com'):
            raise ValidationError("We only accept .com email addresses.")
        return email

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if len(subject.strip()) < 5:
            raise ValidationError("Subject must be at least 5 characters long.")
        return subject

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message.strip()) < 10:
            raise ValidationError("Message must be at least 10 characters long.")
        if "http" in message.lower() or "www" in message.lower():
            raise ValidationError("Links are not allowed in the message.")
        return message

    def clean(self):
        """
        Perform cross-field validation.
        Example: Don't allow the name to appear in the subject.
        """
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        subject = cleaned_data.get('subject')

        if name and subject and name.lower() in subject.lower():
            raise ValidationError("Subject should not contain your name.")

        return cleaned_data
