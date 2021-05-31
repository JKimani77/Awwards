from django.test import TestCase
from .models import Project, Profile, Vote
from django.contrib.auth.models import User
# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        self.marya = User(username="marya", password="1234")
        self.profile = Profile(user = self.marya, prof_pic='png', link='www.prof.com')
        self.marya.save()
        self.profile.save_profile()
 
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.marya, User))
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_user(self):
        self.marya.save()

    def test_delete_user(self):
        self.marya.delete()

    def test_edit_bio(self):
        self.profile.edit_bio('Software Developer')
        self.assertEqual(self.profile.bio, 'Software Developer')

class ProjectTest(TestCase):
    def setUp(self):
        self.marya = User(username = "marya", email = "marya@gmail.com",password = "1234")
        self.profile = Profile(user= self.marya, prof_pic='png',bio='bio', email='marya@gmail', link='www.prof.com')
        self.project = Project(project_title= "test", project_image = "imageurl", project_description ="test project", link = "testlink")

        self.marya.save()
        self.profile.save_profile()
        self.project.save_project()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Project.objects.all().delete()

    def test_image_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_project(self):
        projects = Project.objects.all()
        self.assertTrue(len(projects)> 0)

    def test_get_user_projects_(self):
        profile_projects = Project.get_user_projects(self.profile.id)
        self.assertEqual(profile_projects[0].name, 'test')
        self.assertEqual(len(profile_projects),1 )

    def test_search_project(self):
        project = Project.search_project('test')
        self.assertEqual(len(project),1)

    def test_display_projects(self):
        projects = Project.display_all_projects()
        self.assertTrue(len(projects) > 0 )

    def test_delete_project(self):
        projects1 = Project.objects.all()
        self.assertEqual(len(projects1),1)
        self.project.delete_project()
        projects2 = Project.objects.all()
        self.assertEqual(len(projects2),0)

