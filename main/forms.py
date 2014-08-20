from django import forms

class NameForm(forms.Form):
	mate = forms.IntegerField(label='Mate')
	mateGranat = forms.IntegerField(label='Mate-Granat')
	mateCola = forms.IntegerField(label='Mate-Cola')
