# Generated by Django 3.1.13 on 2021-12-03 17:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "term_letter",
                    models.CharField(
                        choices=[
                            ("A", "A-Term"),
                            ("B", "B-Term"),
                            ("C", "C-Term"),
                            ("D", "D-Term"),
                            ("E", "E-Term"),
                            ("F", "Fall Semester"),
                            ("S", "Spring Semester"),
                        ],
                        max_length=1,
                        verbose_name="Term Letter (the 'A' from A21, A22, etc...)",
                    ),
                ),
                (
                    "term_year",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(18),
                            django.core.validators.MaxValueValidator(35),
                        ],
                        verbose_name="Term Year (the '21' from A21, B21, etc...)",
                    ),
                ),
                (
                    "department",
                    models.CharField(
                        choices=[("CS", "Computer Science")], max_length=3
                    ),
                ),
                (
                    "code",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(500),
                            django.core.validators.MaxValueValidator(5999),
                        ],
                        verbose_name="Course Code",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
