from django.shortcuts import render


def index(request):
    return render(request, "index.html")   # django just renders this page and don't need to specify anything else
