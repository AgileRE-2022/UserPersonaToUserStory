from attr import field, fields
from django.forms import ModelForm
from account.models import UserPersona

class FormConvert(ModelForm) :
    class Meta:
        model = UserPersona
        fields = '__all__'
