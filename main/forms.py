from django import forms

class NameForm(forms.Form):
	MA = forms.IntegerField(label='Mate', widget=forms.TextInput(attrs={'name': 'Mate', 'class': "form-control input-number", 'min': '0', 'max': '10' }))
	MG = forms.IntegerField(label='Mate-Granat', widget=forms.TextInput(attrs={'name': 'Mate-Granat', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
	MC = forms.IntegerField(label='Mate-Cola', widget=forms.TextInput(attrs={'name': 'Mate-Cola', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
	BI = forms.IntegerField(label='Bier', widget=forms.TextInput(attrs={'name': 'Bier', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
	SO = forms.IntegerField(label='Sonstiges', widget=forms.TextInput(attrs={'name': 'Sonstiges', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
	LG = forms.IntegerField(label='Leergut', widget=forms.TextInput(attrs={'name': 'Leergut', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
