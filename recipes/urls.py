from django.urls import path

from recipes.views import home

# URLS do app recipes
urlpatterns = [
    path('', home),
]
