from django.shortcuts import render

def ceapp(request):
    return render(request, "ceapp.html", {})