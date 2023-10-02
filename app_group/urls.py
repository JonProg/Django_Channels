from django.urls import path
from app_group import views

app_name = 'app_group'

urlpatterns = [
    path("", views.index, name="index"),
    path("chat/<slug:group_slug>",views.group, name="group"),
    path('save_message/', views.save_message, name='save_message'),
]