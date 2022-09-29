from django.shortcuts import render,redirect

from .models import Tasks,Users
from django.contrib import messages

from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        messages.info(request,"Login required to access this page")
        return redirect('/login')

    if request.method=="GET":
        print(request.user.id)
        all_tasks=Tasks.objects.filter(user_id=request.user.id,completed=False).all()
        if all_tasks.first():
            return render(request,"home.html",{"all_tasks":all_tasks})
        else:
            messages.info(request,"You haven't created any task")
            return render(request, "home.html", {"all_tasks": None})
    if request.method=="POST":
        #user=Users.objects.get(id=1)
        print(request.user.id)
        task=Tasks(task_name=request.POST['newtask'],user_id=request.user)
        task.save()
        messages.success(request,"New Task Added successfully")
        return redirect('/')


def completed(request):
    if not request.user.is_authenticated:
        messages.info(request,"Login required to access this page")
        return redirect('/login')

    all_tasks=Tasks.objects.filter(user_id=request.user.id,completed=True).all()
    if all_tasks.first():
        return render(request, "complated_tasks.html", {"all_tasks": all_tasks})
    else:
        messages.info(request, "You have 0 completed task")
        return render(request, "complated_tasks.html", {"all_tasks": None})


def complete(request,id):
    if not request.user.is_authenticated:
        messages.info(request,"Login required to access this page")
        return redirect('/login')
    task = Tasks.objects.get(id=id)
    if task:
        task.completed = True
        task.save()
        messages.info(request, "Saved Successfully")
        return redirect('/')
    else:
        messages.info(request, "No task with given id")
        return redirect('/')


def update(request,id):
    if not request.user.is_authenticated:
        messages.info(request,"Login required to access this page")
        return redirect('/login')
    if request.method=="GET":
        task=Tasks.objects.get(id=id)
        if task:
            return render(request, "update_task.html",{"task":task})
        else:
            return redirect('/')
    if request.method=="POST":
        task = Tasks.objects.get(id=id)
        if task:
            task.task_name=request.POST['newtask']
            task.save()
            messages.info(request, "Task Updated Successfully")
            return redirect('/')
        else:
            messages.info(request, "No task with given id")
            return redirect('/')


def delete(request,id):
    if not request.user.is_authenticated:
        messages.info(request,"Login required to access this page")
        return redirect('/login')
    task = Tasks.objects.get(id=id)
    if task:
        task.delete()
        messages.success(request,"Task Deleted Successfully")
        return redirect('/')
    else:
        messages.info(request, "No task with given id")
        return redirect('/')

def completed_delete(request,id):
    if not request.user.is_authenticated:
        messages.info(request,"Login required to access this page")
        return redirect('/login')
    task = Tasks.objects.get(id=id)
    if task:
        task.delete()
        messages.success(request,"Task Deleted Successfully")
        return redirect('/completed')
    else:
        messages.info(request, "No task with given id")
        return redirect('/completed')


def login(request):
    if request.method=="POST":
        username = request.POST['email']
        password = request.POST['password']
        #user = Users.objects.get(username=username)
        # if user:
        #     #login(request, user)
        #     if user.password==password:
        #         request.session['username']=user.username
        #         messages.success(request,"Logged in successfully")
        #         return redirect('/')
        #     else:
        #         messages.info(request, "Incorrect password")
        # else:
        #     messages.info(request, "Invalid Credential")
        #     return redirect('/login')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, "Logged in successfully")
            return redirect('/')
        else:
            messages.info(request, "Invalid Credential")
            return redirect('/login')
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        username = request.POST['email']
        password = request.POST['password1']
        con_password = request.POST['password2']
        if Users.objects.filter(username=username).exists():
            messages.info(request, "Username Taken")
            return redirect('/register')
        if password!=con_password:
            return redirect('/register')
        else:
            new_user=User.objects.create_user(username=username,password=password,first_name=firstname)
            new_user.save()
            return redirect('/login')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    messages.info(request, "Logged Out successfully")
    return redirect('/login')

