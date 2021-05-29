from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profile/<profile_id>', views.profile, name = 'profile'),
    path('add_project/',views.add_project, name = 'add_project'),
    
]
