# Generated by Django 3.2.19 on 2023-05-30 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asosiy', '0004_auto_20230530_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talaba',
            name='user',
        ),
        migrations.AddField(
            model_name='talaba',
            name='user_fk',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
