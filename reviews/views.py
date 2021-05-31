from django.http.response import Http404, HttpResponseRedirect
from reviews.forms import CreateProfileForm, NewProjectForm, RatingProjectForm
from django.shortcuts import render, redirect
import datetime as dt
from .models import Profile, Project, Vote
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

# Create your views here.
def index(request):
    date = dt.date.today()
    projects = Project.display_all_projects()

    return render(request, 'index.html', {"date": date, "projects":projects})

@login_required(login_url='/accounts/login/')
def search_projects(request):
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_projects = Project.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


def get_project(request, id):
    try:
        project = Project.objects.get(pk = id)
        user = User.objects.get(pk = request.user.id)
        profile = Profile.objects.get(user = user)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, "project.html", {"project":project, 'profile':profile})
  

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.Author = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'add_new_project.html', {"form": form})


@login_required(login_url='/accounts/login/')
def user_profiles(request):
    current_user = request.user
    Author = current_user
    projects = Project
    
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile')
        
    else:
        form = CreateProfileForm()
    
    return render(request, 'profile.html', {"form":form})

