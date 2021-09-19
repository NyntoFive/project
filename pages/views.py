from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "pages/homepage.html"

class AboutpageView(TemplateView):
    template_name = "pages/about.html"

class KnowledgeBaseView(TemplateView):
    template_name = "pages/kb.html"