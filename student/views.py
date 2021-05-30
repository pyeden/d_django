from django.shortcuts import render

# Create your views here.


def index(request):
    words = 'World'
    return render(request, 'student/index.html', locals())
