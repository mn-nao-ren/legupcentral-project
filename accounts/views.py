from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def choice(request):
    return render(request, 'accounts/choice.html')


def characterform(request):
    if request.method == 'POST':
        if request.POST['chartype'] == "adult":
            return render(request, 'accounts/adult.html')
        elif request.POST['chartype'] == "student":
            return render(request, 'accounts/student.html')


def adultsignup(request):
    if request.method == 'POST':
        if request.POST['pwd1'] == request.POST['pwd2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/adult.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['pwd1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/adult.html', {'error': 'Passwords must match'})
    else:
        return render(request, 'accounts/adult.html')


def studentsignup(request):
    if request.method == 'POST':
        if request.POST['pwd1'] == request.POST['pwd2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/student.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['pwd1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/student.html', {'error': 'Passwords must match'})
    else:
        return render(request, 'accounts/student.html')


def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['pwd1'] == request.POST['pwd2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['pwd1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
