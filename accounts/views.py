from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from .forms import UpdateProfileForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            form = SignUpForm()
            return render(request, 'accounts/signup.html', {'form': form})

@login_required
def user_dashboard(request):
    return render(request, 'accounts/dashboard.html')

def send_verification_email(user):
    token = default_token_generator.make_token(user)
    uid = urlssafe_base64_encode(user.pk.encode())
    verification_link = f"{request.build_absolute_uri('/verify_email')}?uid={uis}&token={token}"
        send_mail(
            'Verify your Email',
            verification_link,
            'from@rxample.com',
            [user.email],
            fail_silently=False,
        )

def user_login(required):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid login'})
            return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'

def reset_password(request, token):
    try:
        #validate token and set new password
        pass
        except Exception as e:
            pass

@login_required
def update_profile(request):
    if request.method == 'POSt':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_dashboard')
        else:
            form = UpdateProfileForm(instance=request.user)
            return redirect(request, 'accounts/update_profile.html', {'form': form})