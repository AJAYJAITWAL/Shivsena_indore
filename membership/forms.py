from django import forms
from membership.models import info


class member_form(forms.ModelForm):
	class Meta :
		model = info
		fields = '__all__'
