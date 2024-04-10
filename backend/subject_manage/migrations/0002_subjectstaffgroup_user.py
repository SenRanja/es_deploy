# encoding=utf-8
# Generated by Django 3.2.23 on 2024-01-27 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subject_manage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectstaffgroup',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='教师'),
        ),
    ]
