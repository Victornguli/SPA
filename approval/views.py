from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic.edit import FormView
from django.views import View as view
from django.core.files.storage import FileSystemStorage

from .forms import UploadForm,ProjectUploadForm
from .models import Document, Project
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
        print("post")
        form = ProjectUploadForm(request.POST, request.FILES)
        fs = FileSystemStorage()
        print (form.errors)
        if form.is_valid():
            print (form.errors)

            project_title = form.cleaned_data.get("project_title")
            project_category = form.cleaned_data.get("project_category")
            description = form.cleaned_data.get("description")
            country = form.cleaned_data.get("country")
            unit = form.cleaned_data.get("unit")
            sub_office = form.cleaned_data.get("sub_office")
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")

            Project.objects.create(project_title=project_title, project_category=project_category, description=description, country=country,sub_office=sub_office, unit=unit ,start_date=start_date,end_date=end_date, status="tech")
            files = request.FILES.getlist("file")
            
            id = Project.objects.latest("id")
            print(project_title,country,sub_office,start_date,end_date)
            # document = form.save()
            for file_name in files:
                document = Document.objects.create(file=file_name, project=id)
                print (file_name)
            return redirect("index")
        else:
            print("invalid")
    else:
        print ("not post")
        form = ProjectUploadForm
    return render(request, "addproject.html", {"form":form})





# class Upload(FormView):
#     form_class = UploadForm
#     template_name = 'result.html'  # Replace with your template.
#     success_url = 'index'  # Replace with your URL or reverse().

#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 print(file)
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

# class Upload(view):
#     def get(self, request):
#         documents = Document.objects.all()
#         return render(self.request, 'result.html', {'documents': documents})

#     def post(self, request):
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             document = form.save()
#             data = {'is_valid': True, 'name': document.file.name, 'url': document.file.url}
#         else:
#             data = {'is_valid': False}
#         return JsonResponse(data)    


# def addProject(request):
#     form = ProjectUploadForm(request.POST)
#     context = {"form":form}
#     return render(request, "submit.html", context)

# class FileFieldView(FormView):
#     form_class = ProjectUploadForm
#     template_name = 'result.html'  # Replace with your template.
#     success_url = '/'  # Replace with your URL or reverse().

#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 print (f)
#                 # def handle_uploaded_file(f):
#                 #     with open('some/file/name.txt', 'wb+') as destination:
#                 #     for chunk in f.chunks():
#                 #         destination.write(chunk)
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)


def handle_uploaded_file(f):
    with open('name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)