from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    return HttpResponse("Hello, world!")


def say_hello_html(request):
    return render(request, "playground/hello.html", {'name':'4반', 'greeting':'반갑다'})

# def say_bye(request):
#     return render(request, "playground/bye.html", {'name':'이대형쌤','greeting':'힘내세요'})

def say_bye(request):
    context = {
        'name' : '김지훈 선생님',
        'bye' : '안녕히'
    }
    return render(request, "playground/bye.html", context = context)