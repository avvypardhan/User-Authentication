from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email Address'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control',  'placeholder':'Enter Your First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control',  'placeholder':'Enter Your Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Your Username'
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['Placeholder'] = 'Enter Your Password'
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].help_text = ''

class UpdateProfileForm(UserChangeForm):
    
    password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'type':'hidden'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)