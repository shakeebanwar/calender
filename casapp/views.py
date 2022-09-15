from django.shortcuts import render

def casapp(request):
    return render(request, "casapp.html", {})