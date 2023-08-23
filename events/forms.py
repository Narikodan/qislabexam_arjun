from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Event

class RegistrationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPES)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'user_type')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name']
