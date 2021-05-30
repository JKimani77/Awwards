from .models import Profile, Project, Vote
from django.forms import ModelForm
from django import forms

class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['profile', 'pub_date', 'voters', 'design_score','usability_score','content_score','average_design','average_usability','average_score']

class RatingProjectForm(ModelForm):
    class Meta:
        model = Vote
        exclude = ['pub_date', 'voter', 'project']

