from django import forms
from django.shortcuts import render, redirect

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

def session(request):
    username = None
    login_form = LoginForm()

    if request.method == 'GET':
        if 'action' in request.GET:
            action = request.GET.get('action')

            if action == 'logout':
                if request.session.has_key('username'):
                    request.session.flush()
                return redirect('login')

        if 'username' in request.session:
            username = request.session['username']
            print(request.session.get_expiry_age())
            print(request.session.get_expiry_date())
    elif request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            if username.strip() == 'gustavojardim' and password.strip() == 'topnelson13@':
                request.session['username'] = username
                print(request)
            else:
                username = None

    return render(request, 'tcc/login.html', {
        'message': 'bla',
        'form': login_form,
        'username': username,
    })
