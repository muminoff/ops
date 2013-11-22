from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ops.models import Paper, Author


def home_page(request):
    return render(request, "home.html")


#@login_required
def papers_page(request):
    context = {
        'papers': Paper.objects.all(),
        'authors': Author.objects.all(),
    }
    return render(request, "papers.html", context)


def about_page(request):
    return render(request, "about.html")


def contrib_page(request):
    return render(request, "contrib.html")
