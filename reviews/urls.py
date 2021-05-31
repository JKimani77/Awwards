from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name= 'index'),
    path('search/', views.search_projects, name='search_results'),
    path('project/', views.get_project, name='project_results'),
    path('new/project', views.new_project, name='new-project'),
    path('accounts/profile/', views.user_profiles, name='profile'),
    path('rate_project/<project_id>',views.rate_project, name = 'rate_project'),
]
