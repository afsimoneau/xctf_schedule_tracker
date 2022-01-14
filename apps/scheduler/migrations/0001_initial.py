# Generated by Django 4.0 on 2021-12-22 17:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
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
                        on_delete=django.db.models.deletion.CASCADE, to="auth.user"
                    ),
                ),
            ],
        ),
    ]
