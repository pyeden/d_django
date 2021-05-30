from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from .forms import StudentForm
from .models import Student


# def index(request):
#     words = 'World'
#     return render(request, 'student/index.html', locals())


def index(request):
    students = Student.get_all()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student:index'))
        else:
            raise ValueError(form.errors)
    else:
        form = StudentForm()

    return render(request, 'student/index.html', locals())
