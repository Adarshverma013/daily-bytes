from django.forms import ModelForm
from django import forms
from diary_app.models import Entry, UserData
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

class EntryForm(ModelForm):
    class Meta: # Meta class is for attach additional information
        model = Entry
        fields = ('title', 'text', )

        # below is done in ModelForm
    """ def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'input is-medium', 'placeholder': 'Enter a title'})
        self.fields['text'].widget.attrs.update({'class': 'textarea', 'id': 'add_textarea', 'placeholder': 'Write here'}) """


class UserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('email', 'username', 'password1', 'password2', )

class NewUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('password1', 'password2', )

class UserUpdateForm(ModelForm):
    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name',)

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = UserData
        fields = ('bio',)

class ContactForm(forms.Form):
    sender = forms.EmailField()
    message = forms.CharField()


class PasswordChangeCustomForm(PasswordChangeForm):
        error_css_class = 'subtitle'
        error_messages = {'password_incorrect':
                  "message here"}

        old_password = PasswordChangeForm.CharField(required=False, label='old_password',
                      widget=PasswordInput(attrs={
                        'class': 'form-control'}),)

        new_password1 = PasswordChangeForm.CharField(required=False, label='new_password1',
                      widget=PasswordInput(attrs={
                        'class': 'form-control'}),)
        new_password2 = PasswordChangeForm.CharField(required=False, label='new_password2',
                      widget=PasswordInput(attrs={
                        'class': 'form-control'}),)