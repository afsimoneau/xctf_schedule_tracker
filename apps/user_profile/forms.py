from django import forms
from django.forms import ModelForm, widgets
from .models import *


class EditProfileForm(ModelForm):
    """
    Form for editing a user
    """

    event_group_1 = forms.ChoiceField(
        choices=Profile.EventGroups.choices, required=True, label="Event Group 1"
    )
    event_group_2 = forms.ChoiceField(
        choices=Profile.EventGroups.choices, required=False, label="Event Group 2"
    )
    year_in_school = forms.ChoiceField(
        choices=Profile.YearInSchool.choices, required=True, label="Year in School"
    )
    degrees = forms.ModelMultipleChoiceField(
        queryset=DegreeAndCert.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Profile
        fields = [
            "event_group_1",
            "event_group_2",
            "year_in_school",
            "degrees",
        ]
