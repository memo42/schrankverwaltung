from django import forms

class NameForm(forms.Form):
	mate = forms.IntegerField(label='Mate', widget=forms.TextInput(attrs={'name': 'Mate', 'class': "form-control input-number", 'min': '0', 'max': '10' }))
	mateGranat = forms.IntegerField(label='Mate-Granat', widget=forms.TextInput(attrs={'name': 'Mate-Granat', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
	mateCola = forms.IntegerField(label='Mate-Cola', widget=forms.TextInput(attrs={'name': 'Mate-Cola', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
	bier = forms.IntegerField(label='Bier', widget=forms.TextInput(attrs={'name': 'Bier', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
	sonstiges = forms.IntegerField(label='Sonstiges', widget=forms.TextInput(attrs={'name': 'Sonstiges', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
	leergut = forms.IntegerField(label='Leergut', widget=forms.TextInput(attrs={'name': 'Leergut', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
