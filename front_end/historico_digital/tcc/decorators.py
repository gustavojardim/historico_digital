import functools

from django.shortcuts import redirect

def login_required(func):
    functools.wraps(func)
    def check_user_login(request, *args, **kwargs):
        if 'user' in request.session:
            return func(request, *args, **kwargs)
        return redirect('login')
    return check_user_login

def vendor_required(func):
    functools.wraps(func)
    def check_user_login(request, *args, **kwargs):
        if request.session['user']['user_type_id'] == 2:
            return func(request, *args, **kwargs)
        return redirect('login')
    return check_user_login
