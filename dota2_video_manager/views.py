# Create your views here.
from django.shortcuts import HttpResponse, render


def index(request):
    return HttpResponse("my first django site!")


def videos(request):
    print(request.GET)
    news = [{"1": 1}, {"1": 2}]
    return render(request, "videos.html", {"news": news})
