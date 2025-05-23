# Generated by Django 5.1.1 on 2024-10-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaptchaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('captcha', models.CharField(max_length=4)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
