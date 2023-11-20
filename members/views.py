from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from .forms import TaskForm, CreateUserForm, UserUpdateForm
from django.db.models import Sum
from django.http import HttpResponseRedirect
import json


@login_required(login_url='members:login')
def test(request):
    return render(request, 'test.html')

@login_required(login_url='members:login')
def dashboard(request):
    if request.user.is_authenticated:
        search_query = ''
        if request.GET.get('search_query'):
            search_query = request.GET.get('search_query')

        user = request.user
        tasks = Task.objects.filter(user = user, name__icontains=search_query).order_by('-id')
        total_count = Task.objects.filter(user = user).count()

        total_amount = Task.objects.filter(user = user).aggregate(Sum('amount'))
        total_paid = Task.objects.filter(user = user, complete=True).aggregate(Sum('amount'))
        total_pending = Task.objects.filter(user = user, complete=False).aggregate(Sum('amount'))

        form = TaskForm()

        if request.method == 'POST':
            user = request.user.id
            name = request.POST.get('name')
            address = request.POST.get('address')
            amount = request.POST.get('amount')
            task_obj = Task(name=name,address=address,amount=amount, user_id=user)
            task_obj.save()
            messages.info(request, 'Created new contact')
                
            return redirect('/')


        context = {'tasks':tasks, 'form':form, 'total_count':total_count, 'total_amount':total_amount, "total_paid": total_paid, "total_pending":total_pending}
        return render(request, 'home.html', context)

@login_required(login_url='members:login')
def addTask(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            user = request.user
            task.user = user
            form.save()
            messages.info(request, 'Created new contact')
            return HttpResponse(status=204)
        else:
            context = {'update_form': form}
            return render(request, 'add_form.html', context)

    context = {'update_form': form}
    return render(request, 'add_form.html', context)

@login_required(login_url='members:login')
def editTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     address = request.POST.get('address')
    #     amount = request.POST.get('amount')
    #     task_obj = Task(name=name,address=address,amount=amount)
    #     task_obj.save()
    #     messages.success(request, 'Updated')
            
    #     return HttpResponse(status=204)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated')
            
            return HttpResponse(status=204)
        else:
            context = {'update_form': form}
            return render(request, 'update_form.html', context)

            
    context = {'update_form': form}
    return render(request, 'update_form.html', context)

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
    