from django.shortcuts import render
import datetime as dt
from .models import Profile, Project, Vote
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    title = 'Awwards'
    date = dt.date.today()
    projects = Project.display_all_projects()
    high_votes = None
    if len(projects)>=1:
        votes = Vote.get_project_votes
        high_votes = votes[:3]

    return render(request, 'index.html', {'date': date, 'title': title, "projects":projects,})

def create_profile(request):
    current_user = request.user
    title = 'Create Profile'
    #if request.method =='POST':
    return render(request, 'create_profile.html')
