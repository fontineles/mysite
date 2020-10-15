from django.http import HttpResponse

def index(request):
    print('Minha primeira view!')
    return HttpResponse('Hello, world!')