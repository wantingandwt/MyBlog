from django.shortcuts import render

# Create your views here.


def index(request):
    'index page'
    return render(request, 'index.html')


def login(request):
    'login page'
    methodtype = request.method
    if methodtype == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        return render(request, 'login.html', {'retinfo': username+'@'+pwd})
    else:
        return render(request, 'login.html', {'retinfo': 'none'})
