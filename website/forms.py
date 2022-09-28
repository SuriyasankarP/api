from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from . models import member

class memberform(forms.ModelForm):
    class Meta:
        model = member
        fields = '__all__'
        #fields =['fname','lname','email','passwd','age']
