from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    #nos permite invocar html de otros directorios
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")



def contact(request):
    return render(request,"core/contact.html")
