from django.shortcuts import render
from .forms import ProjectUploadForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def addProject(request):
    form = ProjectUploadForm(request.POST)
    context = {"form":form}
    return render(request, "submit.html", context)

