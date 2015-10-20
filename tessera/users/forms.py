from django import forms
from django.contrib.auth.models import User
from users.models import Picture, UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    user_extended = forms.CharField(required=False)
    class Meta:
        model = UserProfile
        fields = ('user_extended',)

class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ('file',)




