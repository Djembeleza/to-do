from django import forms
from .models import (MyUser)


class MyUserForm(forms.ModelForm):
    email2 = forms.EmailField(label="Confirm Email")
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'email2', 'password')

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError('Emails must match.')

        email_qs = MyUser.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                'Email address has already registered.')

        return email
