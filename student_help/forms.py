from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class StageForm(forms.ModelForm):
  class Meta:
    model = Stage
    fields = ['type','typeStg','company','user','period','topic','contactInfo','specialty','image']
