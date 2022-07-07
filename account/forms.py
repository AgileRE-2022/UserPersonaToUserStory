from attr import field, fields
from django.forms import ModelForm
from django import forms
from matplotlib import widgets
from account.models import UserPersona

class FormConvert(forms.ModelForm) :
    class Meta:
        model = UserPersona
        fields = '__all__'
        widgets = {
          'needs': forms.Textarea(attrs={'rows':4, 'cols':15}),
          'goals': forms.Textarea(attrs={'rows':4, 'cols':15}),
          'bio': forms.Textarea(attrs={'rows':4, 'cols':15}),
          'frustrations': forms.Textarea(attrs={'rows':4, 'cols':15}),
          'behaviours': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }