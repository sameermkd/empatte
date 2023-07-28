from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("employee", views.employee, name="employee"),
    path("jobs", views.jobs, name="jobs"),
    path("startingtime", views.startingtime, name="startingtime"),
    path("list", views.ResultList, name="list"),
    
]