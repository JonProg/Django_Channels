from django.urls import path
from app_group import views

app_name = 'app_group'

urlpatterns = [
    path("", views.index, name="index"),
    path("chat/<slug:root>", name="group")
]