from django import forms
from django.utils.safestring import mark_safe

from main.models import Typ
from main.models import Kasten
from main.models import Schrank

maxAnzahl = 100
class NameForm(forms.Form):
	mylabel = {}
	mylabel['Mate'] = mark_safe('<a href="../MA">Mate</a>')
	mylabel['Mate-Granat'] = mark_safe('<a href="../MG">Mate-Granat</a>')
	mylabel['Mate-Cola'] = mark_safe('<a href="../MC">Mate-Cola</a>')
	mylabel['Mate-Eistee'] = mark_safe('<a href="../ME">Mate-Eistee</a>')
	mylabel['Bier'] = mark_safe('<a href="../BI">Bier</a>')
	mylabel['Sonstiges'] = mark_safe('<a href="../SO">Sonstiges</a>')
	mylabel['Leergut'] = mark_safe('<a href="../LG">Leergut</a>')

	MA = forms.IntegerField(label=mylabel['Mate'], widget=forms.TextInput(attrs={'name': 'MA', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl }))
	MG = forms.IntegerField(label=mylabel['Mate-Granat'], widget=forms.TextInput(attrs={'name': 'MG', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))
	MC = forms.IntegerField(label=mylabel['Mate-Cola'], widget=forms.TextInput(attrs={'name': 'MC', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))
	ME = forms.IntegerField(label=mylabel['Mate-Eistee'], widget=forms.TextInput(attrs={'name': 'ME', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))
	BI = forms.IntegerField(label=mylabel['Bier'], widget=forms.TextInput(attrs={'name': 'BI', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))
	SO = forms.IntegerField(label=mylabel['Sonstiges'], widget=forms.TextInput(attrs={'name': 'SO', 'class': "form-control input-number", 'min': '0', 'max': maxAnzahl  }))
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
		SO = self.cleaned_data['SO']
		if SO > maxAnzahl:
			raise forms.ValidationError("Mate out of bounds exception")
		return SO
	def clean_LG(self):
		LG = self.cleaned_data['LG']
		if LG > maxAnzahl:
			raise forms.ValidationError("Mate out of bounds exception")
		return LG

class TypeForm(forms.Form):
	L1 = 'E201'
	L2 = 'E302'
	L3 = 'E303'
	L4 = 'E304'
	L5 = 'E306'
	L6 = 'E013'
	mylabel = {}
	mylabel[L1] = mark_safe('<a href="../' + L1 + '">' + L1 + '</a>')
	mylabel[L2] = mark_safe('<a href="../' + L2 + '">' + L2 + '</a>')
	mylabel[L3] = mark_safe('<a href="../' + L3 + '">' + L3 + '</a>')
	mylabel[L4] = mark_safe('<a href="../' + L4 + '">' + L4 + '</a>')
	mylabel[L5] = mark_safe('<a href="../' + L5 + '">' + L5 + '</a>')
	mylabel[L6] = mark_safe('<a href="../' + L6 + '">' + L6 + '</a>')

	E201 = forms.IntegerField(label=mylabel[L1], widget=forms.TextInput(attrs={'name': L1, 'class': "form-control input-number"}))
	E302 = forms.IntegerField(label=mylabel[L2], widget=forms.TextInput(attrs={'name': L2, 'class': "form-control input-number"}))
	E303 = forms.IntegerField(label=mylabel[L3], widget=forms.TextInput(attrs={'name': L3, 'class': "form-control input-number"}))
	E304 = forms.IntegerField(label=mylabel[L4], widget=forms.TextInput(attrs={'name': L4, 'class': "form-control input-number"}))
	E306 = forms.IntegerField(label=mylabel[L5], widget=forms.TextInput(attrs={'name': L5, 'class': "form-control input-number"}))
	E013 = forms.IntegerField(label=mylabel[L6], widget=forms.TextInput(attrs={'name': L6, 'class': "form-control input-number"}))
