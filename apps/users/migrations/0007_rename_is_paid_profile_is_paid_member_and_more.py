# Generated by Django 4.0.1 on 2022-11-12 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_inspo_profile_is_paid_profile_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_paid',
            new_name='is_paid_member',
        ),
        migrations.AddField(
            model_name='profile',
            name='is_leadership',
            field=models.BooleanField(default=False),
        ),
    ]
