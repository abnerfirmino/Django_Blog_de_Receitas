from django.urls import path

from . import views

# Pattern App name
app_name = 'recipes'

# URLS do app recipes
urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/', views.category, name="category"),  # noqa E501
    path('recipe/<int:id>/', views.recipe, name="recipe"),
]
