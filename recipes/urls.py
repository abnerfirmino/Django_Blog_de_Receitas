from django.urls import path

from . import views

# Pattern App name
app_name = 'recipes'

# URLS do app recipes
urlpatterns = [
    path('', views.home, name="home"),
    path('recipe/category/<int:category_id>/', views.category, name="category"),
    path('recipe/<int:id>/', views.recipe, name="recipe"),
]
