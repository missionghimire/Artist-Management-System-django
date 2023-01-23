from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class AdminForm(UserCreationForm):
    class Meta:
        model = User
        fields=('first_name','last_name','email','phone','dob','gender','address')
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
         }




class UserForm(forms.ModelForm):
    class Meta:
        model=Artist
        exclude=['create_at','updated_at']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'first_release_year': forms.DateInput(attrs={'type': 'date'}),

            
         }



class ArtistForm(forms.ModelForm):
    class Meta:
        model=Music
        exclude=['create_at','updated_at']



class ArtistUpdateForm(forms.ModelForm):
    class Meta:
        model=Music
        exclude=['artist','create_at','updated_at']      