"""
URL configuration for Textutils project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from .import views
# from MyCodes import pipeline

# This path for views.py file
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('analyzer',views.analyzer,name='analyzer')
    ]

# urls setting for pipelines files
# urlpatterns = [
#     path('admin/',admin.site.urls),
#     path('',pipeline.index,name="index"),
#     path('Shivendra',pipeline.Shivendra,name="Shivendra"),
#     path('Pratap',pipeline.Pratap,name="Pratap"),
#     path('Singh',pipeline.Singh,name="Singh"),
#     path('Chauhan',pipeline.Chauhan,name="Chauhan"),
#     path('Fullname',pipeline.Fullname,name="Fullname")
# ]
