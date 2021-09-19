from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Recipe

class RecipePageView(TemplateView):
    template_name = "recipes/detail-page.html"

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/list-view.html"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/detail-view.html"