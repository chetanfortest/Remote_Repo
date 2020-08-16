from django import forms
from django.contrib.auth.models import User
from testapp.models import Movies
# from django.core.exceptions import ValidationError

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email Id'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']

    def clean(self):
        cleaned_data = super().clean()
        inputuser = cleaned_data['username']
        if len(inputuser) < 4:
            raise forms.ValidationError("Length must be greater than 4")

        inputmail = cleaned_data['email']
        if ('.com' not in inputmail):
            raise forms.ValidationError("Invalid Email Id")

        inputpass = cleaned_data['password']
        if len(inputpass)<9:
            raise forms.ValidationError("Length of Password must be or greater than 9")

        inputfirst = cleaned_data['first_name']
        if len(inputfirst) < 3 or (not(inputfirst.isalpha())):
            raise forms.ValidationError("Length of First Name must be greater than 3 and should not contain any digit or special character")


class AddMovieForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        base_lang = ['Kannada','Hindi','Telugu']
        inputlang = cleaned_data['language'].title()
        if inputlang not in base_lang:
            raise forms.ValidationError("Please Enter Correct language ['Kannada','Hindi','Telugu']")

        inputurl = cleaned_data['url']
        if "youtube.com" not in inputurl:
            raise forms.ValidationError("Must be Youtube URL")

    class Meta:
        model = Movies
        fields = '__all__'
