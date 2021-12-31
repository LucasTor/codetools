from django.shortcuts import render

def apis(request):
    return render(request, "apis.html")

def open_source_tools(request):
    return render(request, "open_source_tools.html")