from django.shortcuts import render


def show_tae(request):
    context = {
        'name': '태민',
        'url': 'https://pbs.twimg.com/media/Emo_oKQU4AEiM39.jpg'
    }
    return render(request, "shinee/member.html", context=context)

def show_on(request):
    context = {
        'name': '온유',
        'url': 'https://img.asiatoday.co.kr/file/2021y/03m/09d/2021030901000924300058811.jpg'
    }
    return render(request, "shinee/member.html", context=context)
