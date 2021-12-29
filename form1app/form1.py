from django import forms
from form1app.models import studentdetails

class studentdetailsform(forms.ModelForm):
	class Meta:
		model = studentdetails
		fields = '__all__'