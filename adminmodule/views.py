from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def projecthomepage(request):
    return render(request, 'projecthomepage.html')

def propertieshomepage(request):
    return render(request, 'propertieshomepage.html')

def agentshomepage(request):
    return render(request, 'agentshomepage.html')

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def signup(request):
    return render(request, 'signup.html')

def signup1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Oops! Username already taken.')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.success(request, 'Account created successfully!')
                return redirect('projecthomepage')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                return redirect('agentshomepage')
            elif len(username) == 4:
                return redirect('propertieshomepage')
            else:
                return redirect('projecthomepage')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'projecthomepage.html')
# admin_module/views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm

from django.shortcuts import render, redirect
from .forms import FeedbackForm  # Import the FeedbackForm class from forms.py

def feedback_form_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_thank_you')  # Redirect to the thank you page
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

def admin_thank_you_view(request):
    return render(request, 'admin_thank_you.html')


# views.py

