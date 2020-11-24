import requests
import copy
import json

from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    pass

def services(request):
    response = requests.get('http://127.0.0.1:8000/chain')
    print(response.json())
    services = response.json()
    print(request.user.is_authenticated, 'bla')

    return render(request, "tcc/services.html", {"services" : services})

def new_service(request):
    if request.method == 'POST':
        request_data = copy.deepcopy(request.POST)
        request_data.pop('csrfmiddlewaretoken')
        requests.post('http://127.0.0.1:8000/new_service', json=json.loads(json.dumps(request_data)))
        return redirect('services')
    else:
        return render(request, "tcc/new_service.html", {"new_service" : "ok"})

def post_new_service(request):
    pass
