from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from MyInstaLikeApp.views import UserLoginView
from MyInstaLikeApp.views import UserRegistrationView  # Use the new app name here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
