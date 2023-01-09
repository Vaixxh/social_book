from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm
from .models import CustomUser, uploaded_files


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = "__all__"


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = "__all__"

class booksForm(ModelForm):
    class Meta:
        model = uploaded_files
        fields = "__all__"
