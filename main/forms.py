from django import forms

class NameForm(forms.Form):
	MA = forms.IntegerField(label='Mate', widget=forms.TextInput(attrs={'name': 'Mate', 'class': "form-control input-number", 'min': '0', 'max': '10' }))
	MG = forms.IntegerField(label='Mate-Granat', widget=forms.TextInput(attrs={'name': 'Mate-Granat', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
	MC = forms.IntegerField(label='Mate-Cola', widget=forms.TextInput(attrs={'name': 'Mate-Cola', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
	BI = forms.IntegerField(label='Bier', widget=forms.TextInput(attrs={'name': 'Bier', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
	SO = forms.IntegerField(label='Sonstiges', widget=forms.TextInput(attrs={'name': 'Sonstiges', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
	LG = forms.IntegerField(label='Leergut', widget=forms.TextInput(attrs={'name': 'Leergut', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))

	def clean_MA(self):
		MA = self.cleaned_data['MA']
		if MA > 10:
			raise forms.ValidationError("Mate out of bounds exception")
		return MA
	def clean_MG(self):
		MG = self.cleaned_data['MG']
		if MG > 10:
			raise forms.ValidationError("Mate out of bounds exception")
		return MG
	def clean_MC(self):
		MC = self.cleaned_data['MC']
		if MC > 10:
			raise forms.ValidationError("Mate out of bounds exception")
		return MC
	def clean_BI(self):
		BI = self.cleaned_data['BI']
		if BI > 10:
			raise forms.ValidationError("Mate out of bounds exception")
		return BI
	def clean_SO(self):
		SO = self.cleaned_data['SO']
		if SO > 10:
			raise forms.ValidationError("Mate out of bounds exception")
		return SO
	def clean_LG(self):
		LG = self.cleaned_data['LG']
		if LG > 10:
			raise forms.ValidationError("Mate out of bounds exception")
		return LG
