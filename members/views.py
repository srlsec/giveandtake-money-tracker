from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import TaskForm, CreateUserForm, UserUpdateForm


# Create your views here.
@login_required(login_url='members:login')
def dashboard(request):
    if request.user.is_authenticated:
        search_query = ''
        if request.GET.get('search_query'):
            search_query = request.GET.get('search_query')

        user = request.user
        tasks = Task.objects.filter(user = user, name__icontains=search_query).order_by('-id')
        total_count = Task.objects.filter(user = user).count()

        form = TaskForm()

        if request.method=='POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.user = user
                form.save()
            messages.info(request, 'Created new contact')
            return redirect('/')

        context = {'tasks':tasks, 'form':form, 'total_count':total_count}
        return render(request, 'home.html', context)

@login_required(login_url='members:login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully')
        return redirect('/')

    context = {'update_form': form}
    return render(request, 'update_task.html', context)

def aboutDeveloper(request):
    return render(request, 'about_us.html')

@login_required(login_url='members:login')
def user_profile(request):

    u_form = UserUpdateForm(instance=request.user)
    # p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
    }
    # return render(request, '<app_name>/user_profile.html')
    return render(request, 'user_profile.html', context)

@login_required(login_url='members:login')
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('/')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('members:dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                messages.success(request, 'Login success')

                return redirect('members:dashboard')
            else:
                messages.error(request, 'Username or Password is incorrect')

        return render(request, 'user_login.html')

def user_logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.error(request, 'You are now logged out')
    return redirect('members:login')
  
def user_register(request):
    if request.user.is_authenticated:
        return redirect('members:dashboard')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('members:login')
        context = {'form':form}
        return render(request, 'user_register.html', context=context)
    