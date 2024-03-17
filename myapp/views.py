from django.shortcuts import render

# Create your views here.
def f1(request):
    return render(request, "e-commerce.html")

def f2(request):
    return render(request, "about.html")

def f3(request):
    return render(request, "services.html")

def f4(request):
    return render(request, "contact.html")

def f5(request):
    return render(request, 'login.html')

def f6(request):
    return render(request, 'register.html')