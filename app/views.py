from django.shortcuts import render

# Create your views here.

def filters(request):
    d={'data':'my name is prathyusha'}
    return render(request,'filters.html',d)
    