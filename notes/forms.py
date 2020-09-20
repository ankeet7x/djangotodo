from django import forms

class ToDoForm(forms.Form):
	titleText = forms.CharField(max_length = 100)
	descText = forms.CharField(max_length = 500)

	def __str__(self):
		return self.titleText