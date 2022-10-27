from django.urls import path

from . import views

# URLS do app recipes
urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]
