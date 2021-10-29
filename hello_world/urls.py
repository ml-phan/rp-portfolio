from django.urls import path
from hello_world import views

urlpatterns = [
    path("", views.hello_world, name="hello_world"),
    path("test", views.hello_world_2, name="hello_world")
]