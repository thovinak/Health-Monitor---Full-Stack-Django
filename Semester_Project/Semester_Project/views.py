from django.shortcuts import render


def index(request):
    data = ""
    context = {
        'data': data
    }
    return render(request, 'index.html', context)
