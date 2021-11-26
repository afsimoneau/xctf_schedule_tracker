from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Course(models.Model):
    user = ForeignKey(User, on_delete=CASCADE)
    TERM_LETTER_CHOICES = [
        ("A", "A-Term"),
        ("B", "B-Term"),
        ("C", "C-Term"),
        ("D", "D-Term"),
        ("E", "E-Term"),
        ("F", "Fall Semester"),
        ("S", "Spring Semester"),
    ]
    term_letter = models.CharField(
        max_length=1,
        choices=TERM_LETTER_CHOICES,
        verbose_name="Term Letter (the 'A' from A21, A22, etc...)",
    )
    term_year = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(35)],
        verbose_name="Term Year (the '21' from A21, B21, etc...)",
    )

    # TODO: add all department codes as choices

    DEPARTMENT_CHOICES = [("CS", "Computer Science")]
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)
    code = models.IntegerField(
        validators=[MinValueValidator(500), MaxValueValidator(5999)],
        verbose_name="Course Code",
    )
    title = models.CharField(max_length=150)
