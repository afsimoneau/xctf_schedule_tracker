# Generated by Django 4.0 on 2022-01-13 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female")], default="M", max_length=1
            ),
        ),
    ]
