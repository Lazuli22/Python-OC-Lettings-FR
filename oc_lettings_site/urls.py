from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
