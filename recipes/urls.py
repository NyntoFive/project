from django.urls import path
from . import views


app_name = "recipes"

urlpatterns = [
    path('', views.RecipePageView.as_view(), name="recipes"),
]