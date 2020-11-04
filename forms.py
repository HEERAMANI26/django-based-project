from django import forms
from .models import *

class Student_form(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    password=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)


    class Meta():
        Model=Student
        fields=['username','password']