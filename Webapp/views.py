from django.http import HttpResponse
def index(request):
    return HttpResponse("Hey there, welcome to django workshop")

def coretabs(request):
    return HttpResponse("welcome to coretabs")

def hey_all(request):
    return HttpResponse("Hello all!")