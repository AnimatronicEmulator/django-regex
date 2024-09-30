from . import views
from django.urls import path

urlpatterns = [
    path("", views.regex_get, name="regex"),
    path("test-regex/", views.regex_post, name="regex-post"),
]