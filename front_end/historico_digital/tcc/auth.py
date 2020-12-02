from django import forms
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .decorators import login_required

import requests
import bcrypt
import json
import os

API_URL = 'http://127.0.0.1:5000'

class LoginForm(forms.Form):
    e_mail = forms.CharField(label='',
                             widget=forms.TextInput(attrs={'class' : 'form-control',
                                                           'placeholder': 'E-mail (e.g, john.doe@gmail.com)'}),
                             required=True)
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Senha'}),
                               required=True)
    # Future Feature
    # remember_me = forms.BooleanField(required = False,
    #                                  label = 'Remember Me',
    #                                  widget=forms.CheckboxInput())

class RegisterForm(forms.Form):
    name = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'class' : 'form-control',
                                                          'placeholder': 'Nome completo ou razão social'}),
                            required=True)
    registration = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'class' : 'form-control',
                                                          'placeholder': 'CPF ou CNPJ'}),
                            required=True)
    e_mail = forms.CharField(label='',
                             widget=forms.TextInput(attrs={'class' : 'form-control',
                                                           'placeholder': 'E-mail (e.g., john.doe@gmail.com)'}),
                             required=True)
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': "Senha (e.g., Abc01@. Não use esta!)",
                                                                 'oninput' : 'validePasswordRequirements()'}),
                               required=True)
    password_1 = forms.CharField(label='Confirm Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Confirme sua senha',
                                                                 'oninput' : 'validatePasswordsMatch()'}),
                               required=True)

class TwoFactorForm(forms.Form):
    code = forms.CharField(label='Please, enter the confirmation code that the Banana Bot has sent to your slack:',
                           widget=forms.TextInput(attrs={'class' : 'form-control',
                                                         'placeholder': 'Confirmation code (check your Slack)'}),
                           required=True)

def auth(request):
    user = None
    message = ''
    login_form = LoginForm()

    if request.method == 'GET':
            user = get_sessioned_user(request)
            if user is not None:
                return redirect('home')
    elif request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            e_mail = login_form.cleaned_data['e_mail']
            password = login_form.cleaned_data['password']

            user = get_logged_user(e_mail, password)

            if user != None:
                request.session['user'] = user
                return redirect('home')
            else:
                message = 'Incorrect e-mail OR password'

    return render(request, 'tcc/login.html', {
        'message': message,
        'form': login_form,
        'user': user,
    })

def logout(request):
    login_form = LoginForm()
    request.session.flush()
    return redirect('login')

def register_user(request):
    user = None
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            name = register_form.cleaned_data['name']
            e_mail = register_form.cleaned_data['e_mail']
            password = register_form.cleaned_data['password']
            password_1 = register_form.cleaned_data['password_1']
            registration = register_form.cleaned_data['registration']

            if password == password_1:
                salt = bcrypt.gensalt()
                hashed_pw = bcrypt.hashpw(password.encode('utf8'), salt)

                param = {'name': name,
                         'registration': registration,
                         'e_mail' : e_mail,
                         'password' : str(hashed_pw),
                         'salt': str(salt) }

                response = requests.post(API_URL + '/register', json=json.loads(json.dumps(param)))

                login_form = LoginForm()

                if response.status_code == 200:
                    return redirect('login')
                elif response.status_code == 403:
                    return render(request, 'tcc/register.html', {
                    'message': 'E-mail already in use',
                    'form': register_form, })

    elif request.method == 'GET':
        user = get_sessioned_user(request)
        if user is not None:
            return redirect('home')

    return render(request, 'tcc/register.html', {
        'message': None,
        'form': register_form,
        'user': None
        })

def get_logged_user(e_mail, password):
    response = requests.get(API_URL + '/login/' + e_mail)
    if response.status_code == 200:
        login_data = response.json()

        stored_pw = login_data['password']
        stored_pw = treat_stringed_bytes_from_database(stored_pw)
        stored_salt = login_data['salt']
        stored_salt = treat_stringed_bytes_from_database(stored_salt)

        hashed_pw = bcrypt.hashpw(password.encode('utf8'), stored_salt)

        if hashed_pw == stored_pw:
            return login_data
        else:
            return None
    else:
        return None

def treat_stringed_bytes_from_database(string):
    string = string.replace("'", "")
    string = string[1:]
    string = string.encode('utf8')
    return string

def get_sessioned_user(request):
    if 'user' in request.session:
        return request.session['user']
    return None
