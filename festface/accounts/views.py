from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .models import Students

def register(request):
    message = ''
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        branch = request.POST.get('branch')
        college = request.POST.get('college')
        state = request.POST.get('state')
        district = request.POST.get('district')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')

        dd,mm,yy = dob.split('-')
        dob = yy+'-'+mm+'-'+dd

        userexists = User.objects.filter(username=username).exists()
        emailexists = User.objects.filter(email=email).exists()
        if userexists == True:
            message = 'Username already taken, please try with another username'
            context = {'message':message}
            return render(request,'accounts/signup.html',context)
        if emailexists == True:
            message = 'Email already exists, please login'
            context = {'message':message}
            return render(request,'accounts/signup.html',context)

        User.objects.create_user(username,email,password)
        user = authenticate(username = username, password = password)
        profile = Students(username=user,firstname=firstname,lastname=lastname,gender=gender,dob=dob,branch=branch,college=college,state=state,district=district,city=city,pincode=pincode,phone=phone)
        profile.save()
        login(request,user)
        return redirect('eventsindex')
    else:
        context = {'message':''}
        return render(request,'accounts/signup.html',context)
