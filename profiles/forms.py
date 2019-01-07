from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

# This form is used for registering a new user

class UserCreateForm(forms.ModelForm):
	password1	= forms.CharField(min_length = 8, max_length = 32, label = 'Password', widget = forms.PasswordInput)
	password2	= forms.CharField(min_length = 8, max_length = 32, label = 'Confirm Password', widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'email')
	    
	# This is the method used to ensure unique mail for every user

	def clean_email(self):
		email = self.cleaned_data.get("email")
		queryset = User.objects.filter(email__iexact = email)

		if queryset.exists():
			raise forms.ValidationError("This email id is already registered")
		return email

	# This is the method used to ensure the consistency of the password

	def clean_password2(self):
		p1 = self.cleaned_data.get("password1")
		p2 = self.cleaned_data.get("password2")

		if p1 and p2 and p1 != p2:
			raise forms.ValidationError("Passwords do not match")
		else:
			ch = ''
			for i in str(p2):
				ascii_val = ord(i)
				if (ascii_val >= 33 and ascii_val <= 47) or (ascii_val >= 58 and ascii_val <= 64) or (ascii_val >= 123 and ascii_val <= 126):
					ch += 's'
				elif ascii_val >= 48 and ascii_val <= 57:
					ch += 'n'
				elif (ascii_val >= 65 and ascii_val <= 90) or (ascii_val >= 97 and ascii_val <= 122):
					ch += 'c'

			if not ('s' in ch and 'n' in ch and 'c' in ch):
				raise forms.ValidationError("Your password must contain any special character, numbers and alphabets")

		return p2

	# This method is called when the user has clicked on the submit button

	def save(self, commit = True):
		user = super(UserCreateForm, self).save(commit = False)
		user.set_password(self.cleaned_data.get("password2"))
		user.is_active	 = False
		user.is_staff	 = False

		if commit:
			user.save()
			user.profile.send_activation_mail()

		return user