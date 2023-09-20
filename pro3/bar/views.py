from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Station, Clerk, Job


class AddEmployee(forms.ModelForm):
    class Meta:
        model = Clerk
        fields = "__all__"

class NewUser(UserCreationForm):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = {"first_name", "last_name", "email", "username", "password1", "password2"}

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('index')
        else:
            return render(request, "bar/signin.html", {'message':"Invalid account"})
        
    return render(request, "bar/signin.html")

@login_required(login_url='signin')
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('signin'))
    
    if request.method == "POST":
        form = AddEmployee(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('staff')
    else:
        form = AddEmployee()
    
    return render(request, "bar/index.html", {'form': form})


def signout(request):
    logout(request)
    return render(request, "bar/signin.html")


def signup(request):
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "bar/signup.html",{'message':"You have been registered successfully"})
    else:
        form = NewUser()
    return render(request, "bar/signup.html", {'form': form})


def change_success(request):
    return render(request, "bar/change_success.html")

def staff(request):
    return render(request,"bar/staff.html", {'staff': Clerk.objects.all()})

def update_employee(request, employee_id):
    employee = Clerk.objects.get(id = employee_id)
    form = AddEmployee(instance=employee)

    if request.method == "POST":
        employee = Clerk.objects.get(id = employee_id)
        form = AddEmployee(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('staff'))
    return render(request, "bar/update_employee.html",{'form':form})

def delete_employee(request, employee_id):
    employee = Clerk.objects.get(id = employee_id)

    if request.method == "POST":
        employee = Clerk.objects.get(id = employee_id)
        employee.delete()
        return HttpResponseRedirect(reverse('staff'))
    
    return render(request, "bar/delete_employee.html")