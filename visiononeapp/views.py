from django.shortcuts import render

def visiononeapp(request):
    return render(request, "visiononeapp.html", {})