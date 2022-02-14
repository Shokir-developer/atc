from django import forms
from .models import AmtcModel

class AmtcForm(forms.ModelForm):
	class Meta:
		model = AmtcModel
		fields = '__all__'

		widgets = {
		'fio': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter FIO'}),
		'sn': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter SN'}),
		'p1': forms.Select(attrs={'class':'form-control'}),
		'p2': forms.Select(attrs={'class':'form-control'}),
		'p3': forms.Select(attrs={'class':'form-control'}),
		'vlan': forms.Select(attrs={'class':'form-control'})
		}