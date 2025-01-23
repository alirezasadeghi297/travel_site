from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class sign_up_form(UserCreationForm):

    email= forms.EmailField(required=True,label="Email Address", widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'}))
    
    class Meta:
        model=User
        fields=['email', 'password1', 'username', 'password2']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Add email to user instance
        if commit:
            user.save()
        return user