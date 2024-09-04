from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import LoginForm, RegisterForm, CategoryForm, TaskForm, CommentForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your views here.

def index(request):
    
    if request.user.is_authenticated:

        categories = Category.objects.filter(user=request.user.id)
        categories_list = []
        tmp = []
        cnt = 0
        for category in categories:
            tmp.append(category)
            cnt += 1
            if cnt % 3 == 0:
                categories_list.append(tmp)
                tmp = []

        if tmp: categories_list.append(tmp)

        context = {
            'categories' : categories_list,
        }
        return render(request, 'main/index.html', context)

    return redirect('login')
def show_tasks(request, name):

    if request.user.is_authenticated:

        id = Category.objects.get(name=name, user=request.user.id).id
        tasks = Task.objects.filter(category=id, user=request.user.id)

        tasks_list = []
        tmp = []
        cnt = 0
        for task in tasks:
            tmp.append(task)
            cnt += 1
            if cnt % 3 == 0:
                tasks_list.append(tmp)
                tmp = []

        if tmp: tasks_list.append(tmp)

        context = {
            'tasks' : tasks_list,
        }
        return render(request, 'main/tasks.html', context)
    
    return redirect('login')

def show_tasks_by_status(request, status):
    if request.user.is_authenticated:
        
        tasks = Task.objects.filter(status=status, user=request.user.id)

        tasks_list = []
        tmp = []
        cnt = 0
        for task in tasks:
            tmp.append(task)
            cnt += 1
            if cnt % 3 == 0:
                tasks_list.append(tmp)
                tmp = []

        if tmp: tasks_list.append(tmp)

        context = {
            'tasks' : tasks_list,
        }
        return render(request, 'main/tasks.html', context)
    
    return redirect('login')

def show_details(request,catid, id):
    if request.user.is_authenticated:

        tasks = Task.objects.filter(id=id, user=request.user.id)
        comments = Comment.objects.filter(task=id).order_by('-date')
        context = {
            'tasks': tasks,
            'comments': comments,
        }

        return render(request, 'main/details.html', context)

    return redirect('login')

def register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')

    else:
        form = RegisterForm() 

    
    return render(request, 'main/register.html', {'form': form})



def login(request):

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')  # Redirect to a success page or home
    else:
        form = LoginForm()

    return render(request, 'main/login.html', {'form': form})

def logout(request):

    if request.method == 'POST':
        auth_logout(request)
        return redirect('login')
    
    return redirect('index')

def create_category(request):

    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':

        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save()
            cat.save()
            return redirect('index')
        
    else:
        form = CategoryForm()

    return render(request, 'main/createcategory.html', {'form':form, 'user_id': request.user.id})


def create_task(request):

    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':

        form = TaskForm(request.POST)
        # cat = get_object_or_404(Category, pk=form.cleaned_data['category'])
        # form.fields['category'] = cat

        if form.is_valid():
            cat = form.save()
            cat.save()
            return redirect('index')
        
    else:
        form = TaskForm()
    print(form)
    return render(request, 'main/createtask.html', {'form':form, 'user_id': request.user.id})


def update_category(request, id):

    if not request.user.is_authenticated:
        return redirect('login')
    
    cat = get_object_or_404(Category, id=id, user=request.user.id)
    if request.method == 'POST':
        form = CategoryForm(request.POST , instance=cat)
        if form.is_valid() :
            form.save()          
            return redirect('index')
        else:
            print(form)
    else:  
        form = CategoryForm(instance=cat)
    return render(request, 'main/updatecategory.html' , {'form':form, 'user_id':request.user.id})

def delete_category(request, id):

    if not request.user.is_authenticated:
        return redirect('login')
    
    cat = get_object_or_404(Category, id=id, user=request.user.id)
    cat.delete()

    return redirect('index')



def update_task(request, cat, id):

    if not request.user.is_authenticated:
        return redirect('login')
    
    task = get_object_or_404(Task, id=id, user=request.user.id)
    if request.method == 'POST':
        form = TaskForm(request.POST , instance=task)
        if form.is_valid() :
            form.save()          
            return redirect('tasks', name=cat)

    else:  
        form = TaskForm(instance=task)
    return render(request, 'main/updatetask.html' , {'form':form, 'user_id':request.user.id})

def delete_task(request, cat, id):

    if not request.user.is_authenticated:
        return redirect('login')
    
    task = get_object_or_404(Task, id=id, user=request.user.id)
    task.delete()

    return redirect('tasks', name=cat)

def create_comment(request, id):

    if not request.user.is_authenticated:
        return redirect('login')
    
    task = get_object_or_404(Task, id=id, user=request.user.id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() :
            form.save()          
            return redirect('details', catid = task.category, id = task.id)

    else:  
        form = CommentForm()
        
    return render(request, 'main/createcomment.html' , {'form':form, 'task': task})