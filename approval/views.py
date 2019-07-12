import os
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic.edit import FormView
from django.views import View as view
from django.core.files.storage import FileSystemStorage

from .forms import UploadForm,ProjectUploadForm, AddCommentForm
from .models import Document, Project, Comment
# Create your views here.

def index(request):
    user = request.user
    if user.is_authenticated:
        projects = Project.objects.all()
        return render(request, "index.html", {"projects":projects, "user":user})
    else:
        return render(request, "index.html")

def AddProject(request):
    if request.method == "POST":
        form = ProjectUploadForm(request.POST, request.FILES)
        fs = FileSystemStorage()
        print (form.errors)#Debug Form errors
        if form.is_valid():
            project_title = form.cleaned_data.get("project_title")
            project_category = form.cleaned_data.get("project_category")
            description = form.cleaned_data.get("description")
            country = form.cleaned_data.get("country")
            unit = form.cleaned_data.get("unit")
            sub_office = form.cleaned_data.get("sub_office")
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")

            Project.objects.create(project_title=project_title, project_category=project_category, description=description, country=country,sub_office=sub_office, unit=unit ,start_date=start_date,end_date=end_date, status="tech")
            #Add default techn   ical review as current project state

            files = request.FILES.getlist("file")
            
            id = Project.objects.latest("id")
            for file_name in files:
                document = Document.objects.create(file=file_name, project=id)
                print (file_name)
            return redirect("index")

    else:
        form = ProjectUploadForm
    return render(request, "addproject.html", {"form":form})


def ProjectDetails(request, project_id):
    project = Project.objects.get(id=project_id)
    documents = Document.objects.filter(project_id=project_id)
    comments = Comment.objects.filter(project_id=project_id)
    docs = []
    for document in documents:
        doc = {}
        url = document.file.url
        name = os.path.basename(url)
        print (url)
        doc = {"name":name,"url":url}

        docs.append(doc)

    print(docs)
    return render(request, "project_detail.html", {"project" : project, "documents":docs, "comments":comments})


def TechnicalReview(request):
    projects = Project.objects.filter(status = "tech")
    user = request.user
    return render(request, "technical_review.html", {"projects":projects, "user":user})


def Comments(request, project_id):
    project  = Project.objects.get(id = project_id)
    user = request.user
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        print(form.errors)
        if user.is_authenticated:
            if form.is_valid:
                comment_text = form.cleaned_data.get("comment")
                new_comment = Comment.objects.create(comment_text=comment_text, sender=user, project=project, status="tech")

                return redirect("comments", project_id)
    else:
        form =  AddCommentForm

    comments = Comment.objects.filter(project_id=project_id, status="tech")
    return render(request, "comments.html", {"project" : project,"comments":comments, "form":form})

