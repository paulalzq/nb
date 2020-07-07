from django import forms

class ContactForm(forms.Form):
	contact_name = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class' : 'form-control'
				}
			)
		)
	contact_email = forms.EmailField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class' : 'form-control'
				}
			)
		)
	form_content = forms.CharField(
		required=True,
		widget=forms.Textarea(
			attrs={
				'class' : 'form-control',
				'rows' : '3'
				}
			)
		)
