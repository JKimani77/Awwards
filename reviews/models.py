import cloudinary
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.fields import IntegerField
from django.db.models.lookups import IntegerGreaterThanOrEqual
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    prof_pic = CloudinaryField('image', null=True)
    link = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def edit_bio(self, new_bio):
        self.bio = new_bio
        self.save()

class Project(models.Model):
    project_title = models.CharField(max_length= 50)
    project_image = CloudinaryField(' screenshot')
    project_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    voters = models.IntegerField(default=0)
    link = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default='1')

    def __str__(self) -> str:
        return self.name

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def voters_count(self):
        return self.voters.count()

    @classmethod
    def display_all_projects(cls):
        return cls.objects.all()

    @classmethod
    def get_user_projects(cls,profile):
        return cls.objects.filter(profile=profile)

    @classmethod
    def search_project(cls,name):
        return Project.objects.filter(name__icontains = name)

    class Meta:
        ordering = ['-pub_date']

class Vote(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name = "votes")
    pub_date = models.DateTimeField(auto_now_add=True)
    voter = models.ForeignKey(Profile, on_delete=models.CASCADE)
    design = models.FloatField(default=0, blank=True)
    content = models.FloatField(default=0, blank=True)
    usability = models.FloatField(default=0, blank=True)

    def save_vote(self):
        self.save()

    def delete_vote(self):
        self.delete()

    @classmethod
    def get_project_votes(cls, project):
        return cls.objects.filter(project = project)

    @classmethod
    def get_project_voters(cls, project):
        return cls.objects.filter(project = project)

    class Meta:
        ordering = ['-pub_date']
        