from django import forms
from django.forms import ModelForm
from first_app.models import Register

class Registerform(forms.ModelForm):
    class Meta:
        model=Register
        fields= "__all__"

#def check(value):
    #if value[0].lower() != 'a':
        #raise forms.ValidationError('Name should start with letter "a"')



#class Registration(forms.Form):
  #  name = forms.CharField(max_length=20, validators=[check])
   # email = forms.CharField(max_length=30)
    #text = forms.CharField(widget=forms.Textarea)
    #password = forms.CharField(widget=forms.PasswordInput, validators=[validators.MinLengthValidator(5)])