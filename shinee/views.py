from django.shortcuts import render


def show_taemin(request):
    context = {
        'name' : '이태민',
        'img_src': 'https://pbs.twimg.com/media/Emo_oKQU4AEiM39.jpg',
    }
    return render(request, 'shinee/멤버.html', context=context)

def show_on(request):
    context = {
        'name': '온유',
        'img_src': 'https://cdnimg.melon.co.kr/cm2/artistcrop/images/006/68/811/668811_20230302154842_org.jpg?7d2c335815b3b39c2c164f9f266bb001/melon/optimize/90',
    }
    return render(request, 'shinee/멤버.html', context=context)
