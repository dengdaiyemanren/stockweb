# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(req):
    return render_to_response('index.html')

def lista(req):
    return render_to_response('demo_form.html')