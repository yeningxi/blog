from django.shortcuts import render

# Create your views here.


def dologin(request):
    print(request.POST)
    return render(request, 'login.html')
