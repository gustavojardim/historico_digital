import requests
import copy
import json

from django.shortcuts import render, redirect
from .decorators import login_required, vendor_required

@login_required
def root(request):
    return redirect("home")

@login_required
def home(request):
    return render(request, "tcc/home.html", {"user" : request.session["user"]})

@login_required
def services(request):
    response = requests.get("http://127.0.0.1:8080/chain/" + request.session["user"]["registration"])
    services = response.json()
    return render(request, "tcc/services.html", {"services" : services,
                                                 "user" : request.session["user"]})

@login_required
@vendor_required
def new_service(request):
    if request.method == "POST":
        request_data = copy.deepcopy(request.POST)
        request_data.pop("csrfmiddlewaretoken")
        request_data.appendlist('vendor_id', request.session['user']['user_id'])
        requests.post("http://127.0.0.1:8080/new_service", json=json.loads(json.dumps(request_data)))
        return redirect("services")
    else:
        return render(request, "tcc/new_service.html", {"user" : request.session["user"]})
