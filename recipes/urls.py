from django.urls import path

from . import views

# URLS do app recipes
urlpatterns = [
    path('', views.home),
    path('recipe/<int:id>/', views.recipe),
]
