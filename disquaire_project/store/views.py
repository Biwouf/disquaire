#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	message = 'Salut tout le monde'
	return HttpResponse(message)

def store(request):
	message = 'Bienvenue sur la page store'
	return HttpResponse(message)
