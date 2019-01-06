from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = (
				'title',
				'text'
			)

	
	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget = forms.TextInput(
				attrs = {
					"class": 'title-input',
					"style": "font-family: 'Josefin Sans', sans-serif;"
				}
			)
		self.fields['text'].widget = forms.Textarea(
				attrs = {
					"class": "text-input",
					"style": "font-family: 'Josefin Sans', sans-serif;"
				}
			)