from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import logout as auth_logout, login
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.

class UserRegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'


    def get_success_url(self):
        return self.request.GET.get('next', '/')
    # def form_valid(self, form):
    #     user = form.get_user()
    #     login(self.request, user)
    #     return redirect('index')

def logout(request):
    auth_logout(request)
    return redirect('index')
