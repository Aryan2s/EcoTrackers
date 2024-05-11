from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def register(request):
    if request.method == "POST":
        Username = request.POST['Username']
        reg_email = request.POST['regEmail']
        reg_password = request.POST['regPassword']
        conPassword= request.POST['conPassword']

        if reg_password == conPassword:
            if User.objects.filter(username=Username).exists():
                return HttpResponse('USERNAME IS ALREADY TAKEN')
            elif User.objects.filter(email=reg_email).exists():
                return HttpResponse('EMAIL IS ALREADY TAKEN')
            else:
                user = User.objects.create_user(username=Username, email=reg_email, password=reg_password)
                # Register successful, redirect to login
                return redirect('login')
        else:
            print('Password is not matching....')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def LoginPage(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        logPassword = request.POST.get('logPassword')
        user = authenticate(request, username=Username, password=logPassword)
        if user is not None:
            login(request, user)
            return redirect('Home')  # Assuming 'Home' is the name of your homepage URL pattern
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'login.html')


def Logout(request):
    auth_logout(request)  # Using the renamed function to avoid conflicts
    return redirect('login')
