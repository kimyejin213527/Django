from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    return HttpResponse("Hello, world!")


def say_hello_html(request):
    return render(request, "playground/hello.html")

def say_bye(request):
    return render(request, "playground/bye.html")