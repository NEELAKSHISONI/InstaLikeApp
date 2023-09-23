from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
 # Adjust this import based on your app's directory structure
from django.contrib.auth.views import LoginView
from .forms import LoginForm  # Use the correct capitalization here
from .forms import RegistrationForm  # Use the correct capitalization here
import uuid
import redis


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

  # Use the login_required decorator to protect the view
from django.shortcuts import render
from django.views import View

from .forms import PostForm  # Import your form class

from django.shortcuts import render, redirect
from django.views import View
from .forms import PostForm  # Import your PostForm

from django_redis import get_redis_connection

def chat_view(request):
    # Create a Redis connection
    redis_conn = get_redis_connection("default")
    
    # Perform Redis operations here
def store_chat_message(redis_conn, chat_room_key, message):
    # Store the message in a Redis data structure (e.g., a list)
    redis_conn.lpush(chat_room_key, message)
def get_chat_history(redis_conn, chat_room_key, max_messages=10):
    # Retrieve chat history (e.g., last 10 messages)
    chat_history = redis_conn.lrange(chat_room_key, 0, max_messages - 1)
    return chat_history


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
    def login_view(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to the 'dashboard' URL
            else:
                # Handle invalid login credentials here
                pass
        return render(request, 'login.html')
    
class ChatView(View):
    def get(self, request):
        # Generate a unique identifier (UUID) for the chat room
        chat_room_id = str(uuid.uuid4())

        # Fetch chat history for the current chat room from the database or Redis
        chat_history = self.get_chat_history(chat_room_id)  # Call the method with self

        # Fetch user information for the current user or participants
        user_info = self.get_user_info(request.user)  # Call the method with self

        # You can add more data to the context dictionary as needed
        context = {
            'chat_history': chat_history,
            'user_info': user_info,
            'chat_room_id': chat_room_id,  # Pass the chat room ID to the template
            # Add other data required by your chat template
        }

        return render(request, 'chat.html', context)

    def get_chat_history(self, chat_room_id):
        # Create a Redis client
        redis_client = redis.StrictRedis(
            host='chathistoryredis-do-user-14562213-0.b.db.ondigitalocean.com',
            port=25061,
            password='AVNS_VePqOdgNdEIZ1QLFgKY',  # Replace with your Redis password
            decode_responses=True,  # Decode responses as strings
        )

        # Retrieve chat history from Redis
        chat_history = redis_client.lrange(f'chat_room_{chat_room_id}', 0, -1)

        # Process chat history as needed
        return chat_history

    def get_user_info(self, user):
        # Implement logic to fetch user information
        # You can replace this with your actual implementation
        # Return user information as needed
        return user  # Placeholder; replace with actual user info
