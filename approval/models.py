from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    unit = models.CharField(max_length=50, default="Nutrition")
    # unit = models.OneToOneField(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class Unit(models.Model):
    unit_name = models.CharField(max_length=50, default="Nutrition")

    def __str__(self):
        return self.unit_name

class TechnicalTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ProjectReviewComitee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ProjectCategory(models.Model):
    project_category = models.CharField(max_length=50)
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_category

class Project(models.Model):
    status = (
        ("new", "New"),
        ("tech", "Technical Review"),
        ("prc_review", "PRC Review"),
        ("prc_meeting", "PRC Meeting"),
        ("nfr", "NFR Created"),
        ("closed", "Closed"),
    )
    project_title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    project_category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    sub_office = models.CharField(max_length=50)
    project_category = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    unit = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=status, default="tech")

    def __str__(self):
        return self.project_title

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Suboffice(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name    

class Document(models.Model):
    file = models.FileField(upload_to='media/documents/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file    


class Comment(models.Model):
    comment_text = models.CharField(max_length=200)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = (
        ("new", "New"),
        ("tech", "Technical Review"),
        ("prc_review", "PRC Review"),
        ("prc_meeting", "PRC Meeting"),
        ("nfr", "NFR Created"),
        ("closed", "Closed"),
    )
    status = models.CharField(max_length=50, choices=status, default="tech")
    add_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.text