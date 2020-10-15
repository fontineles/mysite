from django.http import HttpResponse

def sobre(request):
    print('Minha primeira view!')
    return HttpResponse('<br><b>Equipe:</b><br> <b>1:</b> Anderson Silva<br><b>2:</b> Lucas Fontineles<br><b>3:</b> Mayk Anderson')

def index(request):
    print('Minha segunda view!')
    return HttpResponse('Helow, world')