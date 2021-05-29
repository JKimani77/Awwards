from .models import Profile, Project, Vote
from django.forms import ModelForm
from django import forms

class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        