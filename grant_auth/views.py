from django.shortcuts import render, redirect, reverse
from django.http.response import JsonResponse
import string
import random
from django.core.mail import send_mail
from .models import CaptchaModel
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model, login,logout

User = get_user_model()


# Create your views here.
@require_http_methods(['GET', 'POST'])
def grant_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                login(request, user)
                if not remember:
                    request.session.set_expiry(0)
                return redirect(reverse('items:login_index'))
            else:
                return redirect(reverse('grant_auth:login'))

def grant_logout(request):
    logout(request)
    return redirect(reverse('items:index'))


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            User.objects.create_user(username=username, email=email, password=password)
            return redirect(reverse('grant_auth:login'))
        else:
            print(form.errors)
            return redirect(reverse('grant_auth:register'))


def send_email_captcha(request):
    # ?email=xxx
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code': 400, 'msg': 'no email'})
    captcha = "".join(random.sample(string.digits, 4))
    CaptchaModel.objects.update_or_create(email=email, defaults={'captcha': captcha})
    sent = send_mail('grant_auth', message=f"注册验证码为{captcha}", recipient_list=[email], from_email=None)
    if sent:
        print('Notification email sent successfully.')
    else:
        print('Failed to send notification email.')
    return JsonResponse({'code': 200, 'msg': 'success'})
