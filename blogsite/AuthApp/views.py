from django.shortcuts import render , redirect
from blogapp.models import *
from django.contrib.auth import *
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from AuthApp.models import CustomUser
from django.contrib.auth import authenticate ,update_session_auth_hash 
from django.contrib import auth

# Create your views here.





def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        gender = request.POST['gender']
        if len(first_name)>10:
            messages.info(request,'first name cannot be more than 10letters')
            return redirect('register')
        
        if len(password)>5:
            # special_characters = "!@#$%^&*()-+?_=,<>./"
            # for i in special_characters:
            #     if i in password:
                    if password == password1:
                        if CustomUser.objects.filter(username=username).exists():
                            messages.info(request,'username already exites')
                            return redirect('register')
                        elif CustomUser.objects.filter(email=email).exists():
                            messages.info(request,'Email already exist')
                            return redirect('register')
                        else:
                            user = CustomUser.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name , gender=gender)
                            user.save()
                            return redirect('login')
                    else:
                        messages.info(request,'password not matching')
                        return redirect('register')
                # else:
                #     messages.info(request,'passwaord must contains any special charactor')
                #     return redirect('register')
        else:
            messages.info(request,'password must be grater than 6 letters')
            return redirect('register')


    else:
        return render(request,'register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Crediential Not Matching')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

        
def changepassword(request):
    if request.method == 'GET':
        cp = PasswordChangeForm(user=request.user)
        return render(request,'changepass.html',{'cp':cp})
    elif request.method == 'POST':
        aa = PasswordChangeForm(user=request.user, data=request.POST)
        if aa.is_valid():
            user = aa.save()
            update_session_auth_hash(request,user)
            return redirect('home')
        return redirect('changepassword')