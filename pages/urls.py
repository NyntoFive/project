from django.urls import path
from .views import HomepageView, AboutpageView, KnowledgeBaseView

app_name = "pages"

urlpatterns = [
    path('help/', KnowledgeBaseView.as_view(), name="help"),
    path('about/', AboutpageView.as_view(), name="about"),
    path('', HomepageView.as_view(), name="home"),
]