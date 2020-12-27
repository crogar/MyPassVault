from django import forms
from django.core import validators
from mydb.models import User


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verifyemail = forms.EmailField(label='Enter Your Email Again')
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verifyemail']

        if email != vmail:
            raise forms.ValidationError("E-mails don't match")


##########################################################################
# Form for Sign up Page! mydb/signup.html                                #
##########################################################################

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
