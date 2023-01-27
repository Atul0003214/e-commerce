from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.views import LogoutView, LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .forms import *
from django.contrib.auth.forms import PasswordResetForm


class LoginClass(LoginView):
    template_name = 'registration/login.html'


class LogoutClass(LogoutView):
    pass

class PasswordResetClass(PasswordResetView):
    template_name = 'registration/password_rest.html'
    form_class = PasswordResetForm

def SignUp(request):
    if request.method == "POST":
        signupForm = createUserForm(request.POST)
        customForm = createUserFormCustome(request.POST)
        context = {'signupForm': signupForm,'customForm':customForm}
        if signupForm.is_valid() and customForm.is_valid():
                user = signupForm.save()
                name = signupForm.cleaned_data.get('username')
                # dob = customForm.cleaned_data.get('DateOfBirth')
                
                cusForm = customForm.save(commit=False)
                cusForm.user = user
                cusForm.save()
                return HttpResponseRedirect('/login/')
        
    else:
        signupForm = createUserForm()
        customForm = createUserFormCustome()
        context = {'signupForm': signupForm,'customForm':customForm}
    return render(request,'registration/signup.html',context)

class PasswordRestDoneClass(PasswordResetDoneView):
    template_name = "registration/password_rest_done.html"

class PasswordResetConfirmViewClass(PasswordResetConfirmView):
    template_name = 'registration/passconfirmview.html'

class PasswordResetCompleteViewClass(PasswordResetCompleteView):
    template_name = 'registration/resetComplete.html'