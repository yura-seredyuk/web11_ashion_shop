from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .models import Profile



def log_in(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:homepage')
        else:
            pass
    return render(request,'myauth/login.html')

def log_out(request):
    logout(request)
    return redirect('myauth:login')

def sign_in(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        email = request.POST['email']
        city = request.POST['city']
        phone = request.POST['phone']
        user = User.objects.create(username=username,
                                    password=password,
                                    email=email,
                                    is_active=True)
        user.set_password(password)
        profile = Profile.objects.create(user=user)
        user.profile.city = city
        user.profile.phone = phone
        profile.save()
        group = Group.objects.get(name='customers')
        group.user_set.add(user)
        user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:homepage')
    return render(request,'myauth/signin.html')

