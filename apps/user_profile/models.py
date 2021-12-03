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
    short_code = models.CharField(max_length=5)

    def __str__(self) -> str:
        return f"{self.short_code} - {self.level}"


class Profile(models.Model):
    """

    Student athlete profile: non-blank year_in_school, in Students group

    Coach profile: blank year_in_school, in Coaches group


    """

    class EventGroups(models.TextChoices):
        DISTANCE = "DST", ("Distance")
        JUMPS = "JMP", ("Jumps")
        MULTI = "MLT", ("Multi")
        SPRINTS = "SPR", ("Sprints")
        THROWS = "THR", ("Throws")

    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    event_group_1 = models.CharField(
        max_length=3, choices=EventGroups.choices, default=EventGroups.DISTANCE
    )
    event_group_2 = models.CharField(
        max_length=3, choices=EventGroups.choices, blank=True
    )

    class YearInSchool(models.TextChoices):
        FRESHMAN = "FR", ("Freshman")
        SOPHOMORE = "SO", ("Sophomore")
        JUNIOR = "JR", ("Junior")
        SENIOR = "SR", ("Senior")
        GRADUATE = "GR", ("Graduate")

    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        blank=True,
        default=YearInSchool.FRESHMAN,
    )

    degrees = models.ManyToManyField(DegreeAndCert)

    def __str__(self) -> str:
        return f"{self.user.get_full_name()}"

    class Meta:
        unique_together = [["event_group_1", "event_group_2"]]
