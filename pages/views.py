from django.shortcuts import render
from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = "pages/homepage.html"

class AboutpageView(TemplateView):
    template_name = "pages/about.html"
