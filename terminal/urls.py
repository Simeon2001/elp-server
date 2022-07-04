from django.urls import path
from terminal import views

urlpatterns = [
    path('add', views.Add_command),
    path('query', views.search_command),
]