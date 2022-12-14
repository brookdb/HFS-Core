# Generated by Django 4.0.1 on 2022-11-12 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='inspo',
            field=models.TextField(blank=True, verbose_name='Inspirations'),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=20, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Biogrophy'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
