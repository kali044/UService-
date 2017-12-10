from django import forms
from django.core.exceptions import ValidationError
import datetime
from .models import Profile, Textbook_Trading, Carpool, Activity, Tutor,  TutorComment, TextbookComment, CarpoolComment, ActivityComment
from .models import PasswordReset

# class PasswordResetForm(forms.ModelForm):
# #fields
# 	class Meta:
# 		model = PasswordReset
# 		fields = '__all__'
		
class EditTitleForm(forms.Form):
	new_title = forms.CharField(help_text = "Enter new title.")

	def clean_new_date(self):
		data = self.cleaned_data['new_title']
		return data

class EditDateForm(forms.Form):
	new_date = forms.DateField(help_text = "Enter a date.")

	def clean_new_date(self):
		data = self.cleaned_data['new_date']

		# Check date is not in the past.
		if data < datetime.date.today():
			raise ValidationError(_('Invalid date - Date in past'))

		return data


# class EditFieldForm(forms.Form):

class EditCostForm(forms.Form):
	new_cost = forms.DecimalField(help_text = "Enter a cost.")

	def clean_new_cost(self):
		data = self.cleaned_data['new_cost']
		# Check cost isn't negative.
		if data < 0:
			raise ValidationError(_('Invalid cost - No negative costs'))

		return data

class EditDescriptionForm(forms.Form):
	new_description = forms.CharField(help_text = "Enter a description.")

	def clean_new_description(self):
		data = self.cleaned_data['new_description']
		return data
class TextbookCommentForm(forms.ModelForm):

    class Meta:
        model = TextbookComment
        fields = ('text',)
class CarpoolCommentForm(forms.ModelForm):

    class Meta:
        model = CarpoolComment
        fields = ('text',)
class TutorCommentForm(forms.ModelForm):

    class Meta:
        model = TutorComment
        fields = ('text',)
class ActivityCommentForm(forms.ModelForm):

    class Meta:
        model = ActivityComment
        fields = ('text',)
