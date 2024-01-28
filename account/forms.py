# account/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Profile

class SignUpForm(UserCreationForm):
    op = forms.CharField(max_length=16, required=False, help_text='OP')  # Nové pole OP

    class Meta:
        model = Profile
        fields = UserCreationForm.Meta.fields + ('op', 'title', 'gender', 'birth_date', 'mobile_number', 'address')