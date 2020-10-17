from argonautes.models import Equipage
from django.forms import ModelForm, TextInput


class EquipageForm(ModelForm):
    class Meta:
        model = Equipage
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    "placeholder": "Charalampos",
                }
            ),
        }
