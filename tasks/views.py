from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Task, Employee,TaskDetail,Project
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg
# Create your views here.

def manager_dashboard(request):
    return render(request, "dashboard.html")
    

def user_dashboard(request):
    return render(request, "user-dashboard.html")

def test(request):
    name =["Mahmud", "Ahmed", "John","Mr. X"]
    count = 0
    for name in name:
        count += 1
    context ={
        "names": name,
        "age": 25,
        "count": count
    }
    return render(request, "test.html", context)


def create_task(request):
    # Get actual Employee objects from the database
    employees = Employee.objects.all()  # Changed from string list to queryset
    form = TaskForm()
    
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
        #""" For Model Form Data """
            form.save()
            return render(request, "task_form.html", {"form": form,"message": "Task created successfully"})


        
   
    context = {"form": form}
    return render(request, "task_form.html", context)


def view_task(request):
   projects = Project.objects.annotate(
        num_task=Count('task')).order_by('num_task')
   return render(request,"show_task.html",{"project":projects})