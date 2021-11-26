from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class DegreeAndCert(models.Model):
    area_of_study = models.CharField(max_length=50)
    LEVELS = [
        ("BA", "Bachelor"),
        ("MI", "Minor"),
        ("CE", "Certificate"),
        ("MA", "Master"),
        ("PH", "PhD"),
    ]
    level = models.CharField(max_length=2, choices=LEVELS)


class Profile(models.Model):
    EVENT_GROUPS = [
        ("SPR", "Sprints"),
        ("JMP", "Jumps"),
        ("DST", "Distance"),
        ("THR", "Throws"),
        ("MLT", "Multi"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event_group_1 = models.CharField(max_length=3, choices=EVENT_GROUPS)
    event_group_2 = models.CharField(max_length=3, choices=EVENT_GROUPS, blank=True)

    YEAR_CHOICES = [
        ("FR", "Freshman"),
        ("SO", "Sophomore"),
        ("JR", "Junior"),
        ("SR", "Senior"),
        ("GR", "Graduate"),
    ]
    year_in_school = models.CharField(max_length=2, choices=YEAR_CHOICES, blank=True)

    degrees = models.ManyToManyField(DegreeAndCert)
    
class TestTable(models.Model):
    test=models.BooleanField()