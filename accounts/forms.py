from django.forms import ModelForm,PasswordInput, EmailInput, TextInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password confirm'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),

        }


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    contact_phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                                      'placeholder': '0123456789',
                                                                                      'type': 'tel', 'pattern':'[0-9]{10}'}))
    comment = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'})
    )


