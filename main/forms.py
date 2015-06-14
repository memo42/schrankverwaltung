from django import forms

from main.models import Typ
from main.models import Kasten
from main.models import Schrank

maxAnzahl = 100
class NameForm(forms.Form):
	typen = Typ.objects.all()
	mylabel = {}
	mylabel['Mate'] = 'Mate'
	mylabel['Mate-Granat'] = 'Mate-Granat'
	mylabel['Mate-Cola'] = 'Mate-Cola'
	mylabel['Mate-Eistee'] = 'Mate-Eistee'
	mylabel['Bier'] = 'Bier'
	mylabel['Sonstiges'] = 'Sonstiges'
	mylabel['Leergut'] = 'Leergut'
	#for i in typen:
	#	print i.name
		#i.name = forms.IntegerField(label=i.name, widget=forms.TextInput(attrs={'name': i.name, 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl }))
	MA = forms.IntegerField(label=mylabel['Mate'], widget=forms.TextInput(attrs={'name': 'MA', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl }))
	MG = forms.IntegerField(label=mylabel['Mate-Granat'], widget=forms.TextInput(attrs={'name': 'MG', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))
	MC = forms.IntegerField(label=mylabel['Mate-Cola'], widget=forms.TextInput(attrs={'name': 'MC', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))
	ME = forms.IntegerField(label=mylabel['Mate-Eistee'], widget=forms.TextInput(attrs={'name': 'ME', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))
	BI = forms.IntegerField(label=mylabel['Bier'], widget=forms.TextInput(attrs={'name': 'BI', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))
	Sonstiges = forms.IntegerField(label=mylabel['Sonstiges'], widget=forms.TextInput(attrs={'name': 'Sonstiges', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))
	LG = forms.IntegerField(label=mylabel['Leergut'], widget=forms.TextInput(attrs={'name': 'LG', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))

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
	def clean_ME(self):
		ME = self.cleaned_data['ME']
		if ME > maxAnzahl:
			raise forms.ValidationError("Mate out of bounds exception")
		return ME
	def clean_BI(self):
		BI = self.cleaned_data['BI']
		if BI > maxAnzahl:
			raise forms.ValidationError("Mate out of bounds exception")
		return BI
	def clean_SO(self):
		Sonstiges = self.cleaned_data['Sonstiges']
		if Sonstiges > maxAnzahl:
			raise forms.ValidationError("Mate out of bounds exception")
		return Sonstiges
	def clean_LG(self):
		LG = self.cleaned_data['LG']
		if LG > maxAnzahl:
			raise forms.ValidationError("Mate out of bounds exception")
		return LG
