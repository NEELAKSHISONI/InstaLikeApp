from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
#from instaapp.views import upload_photo
from django.urls import path
from instaapp.views import DashboardView
from instaapp.views import ChatView
from django.contrib.auth import views as auth_views


from instaapp.views import UserLoginView
from instaapp.views import UserRegistrationView  # Use the new app name here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),path('logout/', UserLogOutView.as_view(), name='logout'),
    path('chat/', ChatView.as_view(), name='chat'),


]
