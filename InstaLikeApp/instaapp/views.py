from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from myinstalikeapp.forms import RegistrationForm
from django.contrib.auth.views import LoginView
from myinstalikeapp.forms import LoginForm

class UserRegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # After registration, you can redirect the user to the login page or any other page.
            return redirect('login')  # Assuming your login URL name is 'login'
        return render(request, 'registration/register.html', {'form': form})

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'
