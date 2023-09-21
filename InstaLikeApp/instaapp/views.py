from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
 # Adjust this import based on your app's directory structure
from django.contrib.auth.views import LoginView
from .forms import LoginForm  # Use the correct capitalization here
from .forms import RegistrationForm  # Use the correct capitalization here

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

  # Use the login_required decorator to protect the view
from django.shortcuts import render
from django.views import View

from .forms import PostForm  # Import your form class

from django.shortcuts import render, redirect
from django.views import View
from .forms import PostForm  # Import your PostForm

class DashboardView(View):
    template_name = 'dashboard.html'  # Template name for the dashboard

    def get(self, request):
        post_form = PostForm()  # Create a new form instance for GET request
        context = {'post_form': post_form}
        # Other view logic...
        return render(request, self.template_name, context)

    def post(self, request):
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            # Process form data and save to the database
            # Redirect to a success page or reload the dashboard
            return redirect('dashboard')

        # If the form is not valid, re-render the dashboard with errors
        context = {'post_form': post_form}
        return render(request, self.template_name, context)



class UserRegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # After registration, you can redirect the user to the login page or any other page.
            return redirect('login')  # Assuming your login URL name is 'login'
        return render(request, 'register.html', {'form': form})

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'



