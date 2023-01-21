from django.urls import path
from django_distill import distill_path
from resume.views import show_main

urlpatterns = [
    distill_path("", show_main, name = "show_main"),
]
