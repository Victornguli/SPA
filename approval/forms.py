from django import forms
from approval.models import ProjectCategory


class ProjectUploadForm(forms.Form):
    countries  = (
        ("Kenya", "Kenya"),
        ("Uganda", "Uganda"),
        ("Rwanda", "Rwanda"),
        ("Tanzania", "Tanzania"),
        ("Burundi", "Burundi"),
        ("Ethiopia", "Ethiopia"),
    )
    counties = (
        ("Nairobi", "Nairobi"),
        ("Nairobi", "Nairobi"),
        ("Nairobi", "Nairobi"),
        ("Nairobi", "Nairobi"),
        ("Nairobi", "Nairobi"),
    )
    project_title = forms.CharField(max_length="50", required=True, widget=forms.TextInput(attrs={'placeholder':'Project Title'}))
    country_office = forms.ChoiceField(choices=countries, required=False)
    sub_office = forms.ChoiceField(choices=counties, required=False)
    project_category = forms.ModelChoiceField(queryset=ProjectCategory.objects.all())
    description = forms.CharField(max_length= "500", required=False, widget=forms.Textarea(attrs={'placeholder':'Description',"cols":2, "rows":2}))
    start_date = forms.DateTimeField(
        required=False,
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))
    
    end_date = forms.DateTimeField(
        required=False,
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))
