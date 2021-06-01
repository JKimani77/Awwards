from django.test import TestCase
from .models import Project, Profile, Vote
from django.contrib.auth.models import User
# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = User(id=1, username='marya', password='1234')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class ProjectTestClass (TestCase):
    def setUp(self):
        self.project = Project.objects.create(project_title='test post',
        project_image='png', project_description='bio',)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Project))

    def test_save_post(self):
        self.post.save_post()
        post = Project.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Project.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.project.save()
        post = Project.search_project('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.project.delete_post()
        project = Project.search_project('test')
        self.assertTrue(len(project) < 1)