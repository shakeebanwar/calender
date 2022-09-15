from django.shortcuts import render

def iwsaasapp(request):
    return render(request, "iwsaasapp.html", {})