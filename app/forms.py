from django import forms
from app.models import *


class student (forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'