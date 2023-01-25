from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields=('first_name','last_name','email','phone','dob','gender','address')
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
         }




class UserupdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('first_name','last_name','email','phone','dob','gender','address')
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
         }


# class UserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         exclude=['create_at','updated_at']
#         widgets = {
#             'dob': forms.DateInput(attrs={'type': 'date'}),
#             'first_release_year': forms.DateInput(attrs={'type': 'date'}),

            
#          }


def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

class ArtistForm(forms.ModelForm):
    first_release_year = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)

    class Meta:
        model=Artist
        exclude=['create_at','updated_at']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
         }



class ArtistUpdateForm(forms.ModelForm):
    class Meta:
        model=Artist
        exclude=['artist','create_at','updated_at']      



class MusicForm(forms.ModelForm):
    class Meta:
        model=Music
        exclude=['artist','create_at','updated_at']      