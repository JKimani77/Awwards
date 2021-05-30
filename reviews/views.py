from django.http.response import Http404, HttpResponseRedirect
from reviews.forms import CreateProfileForm, NewProjectForm, RatingProjectForm
from django.shortcuts import render, redirect
import datetime as dt
from .models import Profile, Project, Vote
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
    if request.method =='POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')
    else:
        form = CreateProfileForm()

    return render(request, 'create_profile.html', {'form': form, 'title':title})

@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    try:
        user = User.objects.get(pk = profile_id)
        profile = Profile.objects.get(user = user)
        title = profile.user.username
        projects = Project.get_user_projects(profile_id)
        projects_count = projects.count()
        votes = []
        for project in projects:
            votes.append(project.average_score)
        total_v = sum(votes)
        average = 0
        if len(projects)>1:
            average = total_v/len(projects)
    except Profile.DoesNotExist:
        raise Http404()
    return render(request, 'profile.html', {'profile':profile, 'projects': projects,'votes': votes, 'average': average, 'total_v':total_v})

@login_required(login_url='/accounts/login/') 
def add_project(request):
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        current_user = request.user
        try:
            profile = Profile.objects.get(user = current_user)
        except Profile.DoesNotExist:
            raise Http404()
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = profile
            project.save()
        return redirect('index')
    else:
        form = NewProjectForm()
    return render(request, 'add_new_project.html', {'form': form})

@login_required(login_url='/accounts/login/')
def search_project(request):
    if "project" in request.GET and request.GET["project"]:
        searched_project = request.GET.get("project")
        voted = False
        try:
            projects = Project.search_project(searched_project)
            number = projects.number()
            message = f"{searched_project}"
            if len(projects) ==1:
                project = projects[0]
                form = RatingProjectForm()
                votes = Vote.get_project_votes(project.id)
                voters = project.voters
        except Profile.DoesNotExist:
            suggestions = Project.display_all_projects()
            message = f"No projects titled found{searched_project}"
            return render(request, 'search.html', {"projects": projects,"message": message, "number":number})
        else:
            message = "You haven't searched"
            return render(request, 'search.html', {"message": message})


