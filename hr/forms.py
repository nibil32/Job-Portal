from django import forms
from myapp.models import category,job

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    
class categoryform(forms.ModelForm):
    class Meta:
        model=category
        fields = ['name']

class jobform(forms.ModelForm):
    class Meta:
        model=job
        # exclude=('salary',)
        fields='__all__'        