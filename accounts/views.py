from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm, RegisterForm
from django.http import HttpResponse
from django.contrib.auth.models import User

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/accounts/login/')



class LoginView(View):
    def get(self , request):
        if request.user.is_authenticated:
            print(user.username)
            user = request.user
            return redirect('/', {"user":user})
        else:
            form = LoginForm()
            return render(request, 'auth/login.html', {'form' : form})
        

    def post(self , request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cleanedData = form.cleaned_data
            user = authenticate(username = cleanedData['username'], password = cleanedData['password'])
            if user:
               login(request, user)
               return redirect('/')
            else:
                return HttpResponse("Invalid Credintials")
        else:
            return HttpResponse("Invalid Form")    


class RegisterView(View):
    def get(self , request):
        if request.user.is_authenticated:
            user = request.user
            return redirect('/', {"user":user})
            
        else:
            form = RegisterForm()
            return render(request, 'auth/register.html', {'form' : form})
    
    def post(self , request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cleanedData = form.cleaned_data
            if cleanedData['password'] == cleanedData['password2']:
                NewUser = User(first_name = cleanedData['first_name'],last_name = cleanedData['last_name'],email = cleanedData['email'], username = cleanedData['username'])
                password = cleanedData['password']
                NewUser.set_password(password)
                NewUser.save()
                user = NewUser 
                login(request, user)
                return redirect('/', {"user":user}) 
            else:
                print("No")
                return HttpResponse("Confirm Password Does not matches")               
        else:
            print("Invalid Form")
            return render(request, 'auth/register.html', {'form' : form})