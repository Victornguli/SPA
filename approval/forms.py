from django import forms
from approval.models import Document, ProjectCategory, Project, Country, Suboffice, Unit


class ProjectUploadForm(forms.Form):
    
    project_title = forms.CharField(max_length="50", required=True, widget=forms.TextInput(attrs={'placeholder':'Project Title'}), help_text="Add The name of the project here" )
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=False, help_text="Select The name of the Country")
    sub_office = forms.ModelChoiceField(queryset=Suboffice.objects.all(), required=False)
    unit = forms.ModelChoiceField(queryset=Unit.objects.all(), required=False, help_text="Select the appropriate unit for the project")
    project_category = forms.ModelChoiceField(queryset=ProjectCategory.objects.all(), help_text="Select The name of the Project Category")
    description = forms.CharField(max_length= "500", required=False, widget=forms.Textarea(attrs={'placeholder':'Description',"cols":2, "rows":2}), help_text="Add a description of your project with less than 400 characters")
    start_date = forms.DateTimeField(
        required=False,
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }), help_text="Enter Start date for this project review")
    
    end_date = forms.DateTimeField(
        required=False,
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }), help_text="Enter End date for this project review")
    file = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}), help_text="Upload document(s) relevant to the project review")


# class FileUploadForm(forms.Form):
#     class Meta:
#         model = Document
#         fields = ["file"]
    

class UploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    # class Meta:
    #     model = Document
    #     fields = ("file",)

class AddCommentForm(forms.Form):
    comment = forms.CharField(max_length=400, required=True, widget=forms.Textarea(attrs={'placeholder':'Write a comment',"cols":70, "rows":5}), help_text="Add Technical Review comments")