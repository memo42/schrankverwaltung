from django import forms

class NameForm(forms.Form):
	mate = forms.IntegerField(label='Mate', widget=forms.TextInput(attrs={'name': 'Mate', 'class': "form-control input-number", 'min': '0', 'max': '10' }))
	mateGranat = forms.IntegerField(label='Mate-Granat', widget=forms.TextInput(attrs={'name': 'Mate-Granat', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
	mateCola = forms.IntegerField(label='Mate-Cola', widget=forms.TextInput(attrs={'name': 'Mate-Cola', 'class': "form-control input-number", 'min': '0', 'max': '10'  }))
