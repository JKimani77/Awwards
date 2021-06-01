from rest_framework import serializers
from . models import Project, Profile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('project_title', 'project_description', 'project_image', 'pub_date', 'link', 'authors')