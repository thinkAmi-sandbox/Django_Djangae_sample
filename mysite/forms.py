from django import forms

from .models import Impression
from .widgets import DateInput

class DetailForm(forms.ModelForm):
    class Meta:
        model = Impression
        fields = '__all__'

        widgets = {
            'registration_date': DateInput(attrs={'class': 'form-control input-sm'}),
        }