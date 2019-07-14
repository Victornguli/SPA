from django import forms
from django.contrib.auth.models import User
from .models import Project, ProjectCategory, Unit
import django_filters

class ProjectFilter(django_filters.FilterSet):
    project_title = django_filters.CharFilter(lookup_expr = "contains")
    description = django_filters.CharFilter(lookup_expr = "contains")
    project_category = django_filters.ModelMultipleChoiceFilter(queryset=ProjectCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    unit = django_filters.ModelMultipleChoiceFilter(queryset=Unit.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    start_date = django_filters.NumberFilter(lookup_expr='year')
    end_date = django_filters.NumberFilter(lookup_expr='year')
    class Meta:
        model = Project
        fields = ['project_title', 'country', 'sub_office', "unit", "description", "unit","project_category","start_date", "end_date"]
