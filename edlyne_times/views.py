from django.shortcuts import render


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'edlyne_times/index.html')


def research(request):
    context = {}
    return render(request, 'edlyne_times/research.html', context)



