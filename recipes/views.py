from django.shortcuts import render
from django.views.generic import TemplateView

class RecipePageView(TemplateView):
    template_name = "recipes/detail-page.html"
