from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # user_category = models.CharField(max_length=50, default="nutrition")
    is_nutrition = models.BooleanField(default = True)

class Nutrition(models.Model):
    group_name = models.CharField(max_length=50, default="nutrition")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name


class ProjectCategory(models.Model):
    project_category = models.CharField(max_length=50)


class Project(models.Model):
    name = models.CharField(max_length=50)
    project_category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.CharField(max_length=200)
    sender = models.ForeignKey(Project, on_delete=models.CASCADE)