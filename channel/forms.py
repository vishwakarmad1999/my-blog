from django import forms
from .models import Channel

class ChannelForm(forms.ModelForm):
	class Meta:
		model = Channel
		fields = (
				'title',
				'description',
			)

	def __init__(self, *args, **kwargs):
		super(ChannelForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget = forms.TextInput(
				attrs = {
					"class": 'title-input',
					"style": "font-family: 'Josefin Sans', sans-serif;"
				}
			)
		self.fields['description'].widget = forms.TextInput(
				attrs = {
					"class": 'title-input',
					"style": "font-family: 'Josefin Sans', sans-serif;"
				}
			)
