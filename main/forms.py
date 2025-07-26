from django import forms
from .models import Contact  # make sure Contact model is defined in models.py

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Your Email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Your Message',
                'rows': 5
            }),
        }
