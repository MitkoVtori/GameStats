from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

from GameStats.Profile.validators import min_length, must_have_digit_and_letter

UserModel = get_user_model()


class AppUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, validators=[min_length, must_have_digit_and_letter])
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["username", "email", "password"]

    def clean(self):
        cleaned_data = super(AppUserCreationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match!")

        return cleaned_data

    def save(self, commit=True):
        user = super(AppUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Invalid username or password!"
        ),
        'inactive': _("This account is inactive."),
    }

    class Meta:
        model = UserModel
        fields = ["username", "password"]
