from . import views
from django.urls import path

urlpatterns = [
    path("", views.re_get, name="re"),
    path("test-re/", views.re_post, name="re-post"),
]