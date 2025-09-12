from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'user_name',
            'user_family',
            'user_email',
            'message_title',
            'message_text'
        ]

    def clean_user_name(self):
        return self.cleaned_data["user_name"]
    
    def clean_user_family(self):
        return self.cleaned_data["user_family"]