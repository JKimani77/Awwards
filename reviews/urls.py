from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name= 'index'),
    path('search_projects/', views.search_projects, name='search_results'),
    path('project/<project_id>', views.display_all_project, name='project'),
    path('new/project', views.new_project, name='new_project'),
    path('profile/', views.user_profiles, name='profile'),
    path('ratings/',include('star_ratings.urls',namespace='ratings')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)