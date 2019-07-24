from django import forms
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    age=forms.IntegerField()
    keep_me_logged_in=forms.BooleanField()