from django.contrib import admin
from .models import Project, Profile, Vote
# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Vote)
