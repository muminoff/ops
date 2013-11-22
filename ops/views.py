from django.shortcuts import render


def home_page(request):
    return render(request, "home.html")


def papers_page(request):
    return render(request, "papers.html")


def about_page(request):
    return render(request, "about.html")


def contrib_page(request):
    return render(request, "contrib.html")
