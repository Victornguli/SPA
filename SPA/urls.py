"""SPA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from approval import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    # path('addProject', views.addProject, name="addProject"),
    path('add_project', views.AddProject, name="add_project"),
    path('^project_details/(?P<project_id>\d+)/$', views.ProjectDetails, name='project_details'),
    path('^technical_review/', views.TechnicalReview, name='technical_review'),
    path('^prc_review/', views.PrcReview, name='prc_review'),
    path('^prc_meeting/', views.PrcMeeting, name='prc_meeting'),
    path('^nfr/', views.NfrCreated, name='nfr'),
    path('^closed/', views.Closed, name='closed'),
    path('^comments/(?P<project_id>\d+)/$', views.Comments, name='comments'),
    path('search/', views.search, name='search'),
    path('^change_status/(?P<project_id>\d+)/<slug:status>/', views.changeProjectStatus, name='change_status'),
    # path('viewer/', views.docPreview, name='viewer'),
    # path('upload', views.Upload, name="upload"),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)