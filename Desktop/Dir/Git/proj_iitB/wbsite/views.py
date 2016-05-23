from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.core.context_processors import csrf
import requests

def home(request):
	return render_to_response('boothome.html')
