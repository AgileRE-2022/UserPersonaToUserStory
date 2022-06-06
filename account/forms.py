from attr import field, fields
from django.forms import ModelForm
from django import forms
from matplotlib import widgets
from account.models import UserPersona

class FormConvert(ModelForm) :
    class Meta:
        model = UserPersona
        fields = '_all_'