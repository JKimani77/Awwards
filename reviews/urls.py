from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profile/<profile_id>', views.profile, name = 'profile'),
    path('add_project/',views.add_project, name = 'add_project'),
    path('project/<project_id>', views.project, name='project'),
    path('search_project/',views.search_project,name = 'search_project'),
    path('rating_project/<project_id>', views.rating_project, name = 'rating_project'),
]
