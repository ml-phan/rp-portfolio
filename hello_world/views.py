from django.shortcuts import render

def hello_world(request):
    return render(request, "hello_world.html", {})

def hello_world_2(request):
    return render(request, "hello_world_2.html", {})

# Create your views here.
