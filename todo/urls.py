from django.urls import path
from . import views
app_name = "todos"

urlpatterns = [
    path("", views.list, name="list"),
    path("create/", views.create, name="create"),
]