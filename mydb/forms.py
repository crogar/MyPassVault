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
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control','type' : 'password'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'email@example.com'}),
        }

    def clean(self):
        all_clean_data = super().clean()
        _user = all_clean_data['user_name']

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(user_name=_user)
            if str(match) == str(_user):
                print('User Already Exist')
                raise forms.ValidationError('This Username is already in use.')
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            pass
