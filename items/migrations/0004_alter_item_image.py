# Generated by Django 5.1.1 on 2024-10-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_item_overdue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='static/images/logo.png', upload_to='items/', verbose_name='图片'),
        ),
    ]
