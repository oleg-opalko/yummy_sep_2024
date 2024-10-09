from cProfile import label

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50, label="Username", widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                              'placeholder': 'Username',
                                                                                              'data-rule': 'username',
                                                                                              'id': 'username',
                                                                                              'autofocus': 'autofocus',
                                                                                              'data-msg': 'Please enter your username'}))

    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                                          'class': 'form-control',
                                                                          'data-msg':'Please enter a valid email address.',
                                                                          'data-rule': 'email',
                                                                          'id': 'email'
                                                                          }))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                                    'class': 'form-control',
                                                                                    'data-rule': 'password',
                                                                                    'id': 'password',
                                                                                    'data-msg': 'Please enter your password.'}))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                                            'class': 'form-control',
                                                                                            'data-rule': 'password',
                                                                                            'id': 'password2',
                                                                                            'data-msg': 'Please confirm your password.'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, label="Username", widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                                              'class': 'form-control',
                                                                                              'data-rule': 'username',
                                                                                              'id': 'username',
                                                                                              'autofocus': 'autofocus'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                                   'class': 'form-control',
                                                                                   'data-rule': 'password',
                                                                                   'id': 'password',
                                                                                   'data-msg': 'Please enter your password.'}))

