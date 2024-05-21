from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')

class StageForm(forms.ModelForm):
  class Meta:
    model = Stage
    fields = ['type','typeStg','company','period','topic','contactInfo','specialty','image']
class AccommodationForm(forms.ModelForm):
  class Meta:
    model = Accommodation
    fields = ['type','location','description','contactInfo','image']    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']   
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }      
class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['type','image', 'begin', 'destination', 'hourBegin', 'nbrSeat']
class RecommandationForm(forms.ModelForm):
    class Meta:
        model = Recommandation
        fields = ['type','image', 'text']
class EventClubForm(forms.ModelForm):
    class Meta:
        model = EventClub
        fields = ['image', 'title', 'description', 'place', 'contactInfo', 'club']            
class EventSocialForm(forms.ModelForm):
    class Meta:
        model = EventSocial
        fields = ['image', 'title', 'description', 'place', 'contactInfo', 'prix']                    

