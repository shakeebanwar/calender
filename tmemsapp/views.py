from django.shortcuts import render

def tmemsapp(request):
    return render(request, "tmemsapp.html", {})