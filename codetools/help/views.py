from django.shortcuts import render

def about(request):
    return render(request, "about.html")

def contrib(request):
    return render(request, "contrib.html")