from django import forms

from main.models import Typ
from main.models import Kasten
from main.models import Schrank

maxAnzahl = 20
class NameForm(forms.Form):
	typen = Typ.objects.all()
	
	for i in typen:
		print i.name
		#i.name = forms.IntegerField(label=i.name, widget=forms.TextInput(attrs={'name': i.name, 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl }))
	MA = forms.IntegerField(label='Mate', widget=forms.TextInput(attrs={'name': 'Mate', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl }))
	MG = forms.IntegerField(label='Mate-Granat', widget=forms.TextInput(attrs={'name': 'Mate-Granat', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))
	MC = forms.IntegerField(label='Mate-Cola', widget=forms.TextInput(attrs={'name': 'Mate-Cola', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))
	BI = forms.IntegerField(label='Bier', widget=forms.TextInput(attrs={'name': 'Bier', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))
	SO = forms.IntegerField(label='Sonstiges', widget=forms.TextInput(attrs={'name': 'Sonstiges', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))
	LG = forms.IntegerField(label='Leergut', widget=forms.TextInput(attrs={'name': 'Leergut', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))

	def clean_MA(self):
		MA = self.cleaned_data['MA']
		if MA > maxAnzahl:
			raise forms.ValidationError("Mate out of bounds exception")
		return MA
	def clean_MG(self):
		MG = self.cleaned_data['MG']
		if MG > maxAnzahl:
			raise forms.ValidationError("Mate out of bounds exception")
		return MG
	def clean_MC(self):
		MC = self.cleaned_data['MC']
		if MC > maxAnzahl:
			raise forms.ValidationError("Mate out of bounds exception")
		return MC
	def clean_BI(self):
		BI = self.cleaned_data['BI']
		if BI > maxAnzahl:
			raise forms.ValidationError("Mate out of bounds exception")
		return BI
	def clean_SO(self):
		SO = self.cleaned_data['SO']
		if SO > maxAnzahl:
			raise forms.ValidationError("Mate out of bounds exception")
		return SO
	def clean_LG(self):
		LG = self.cleaned_data['LG']
		if LG > maxAnzahl:
			raise forms.ValidationError("Mate out of bounds exception")
		return LG
