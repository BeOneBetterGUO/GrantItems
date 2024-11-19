from django import forms

from .models import CaptchaModel
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2, error_messages={
        'required': '用户名不能为空',
        'max_length': '用户名最大长度为20',
        'min_length': '用户名最小长度为2'
    })
    email = forms.EmailField(error_messages={"required": "邮箱不能为空", "invalid": "邮箱格式错误"})
    captcha = forms.CharField(max_length=4, min_length=4, error_messages={
        'required': '验证码不能为空',
        'max_length': '验证码长度为4',
        'min_length': '验证码长度为4'
    })
    password = forms.CharField(max_length=20, min_length=6, error_messages={
        'required': '密码不能为空',
        'max_length': '密码最大长度为20',
        'min_length': '密码最小长度为6'
    })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱已经存在')
        return email

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        email = self.cleaned_data.get('email')
        captcha_model = CaptchaModel.objects.filter(email=email, captcha=captcha).first()
        if not captcha_model:
            raise forms.ValidationError('验证码错误')
        captcha_model.delete()
        return captcha

class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={"required": "邮箱不能为空", "invalid": "邮箱格式错误"})
    password = forms.CharField(max_length=20, min_length=6, error_messages={
        'required': '密码不能为空',
        'max_length': '密码最大长度为20',
        'min_length': '密码最小长度为6'
    })
    remember = forms.IntegerField(required=False)
