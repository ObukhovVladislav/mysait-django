from django.shortcuts import render


def index(request):
    return render(request, 'myapp/index.html')

def catalog(request):
    return render(request, 'myapp/catalog.html')

def basket(request):
    return render(request, 'myapp/basket.html')
