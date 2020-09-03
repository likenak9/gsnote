from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "사용자 이름"
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
        })
    
        self.fields['email'].label = "e-mail"
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['password1'].label = "비밀번호"
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['password2'].label = "비밀번호 확인"
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
        })
        
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'class' : 'form-control', 
            }
        )
    )