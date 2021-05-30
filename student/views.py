# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.urls import reverse
#
# from .forms import StudentForm
# from .models import Student
#
#
# # def index(request):
# #     words = 'World'
# #     return render(request, 'student/index.html', locals())
#
#
# def index(request):
#     students = Student.get_all()
#
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('student:index'))
#         else:
#             raise ValueError(form.errors)
#     else:
#         form = StudentForm()
#
#     return render(request, 'student/index.html', locals())


from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import StudentForm
from .models import Student


# def index(request):
#     words = 'World'
#     return render(request, 'student/index.html', locals())

class IndexView(View):

    template = 'student/index.html'

    def get(self, request):

        form = StudentForm()
        students = Student.get_all()

        return render(request, self.template, locals())

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student:index'))

        return render(request, self.template, locals())
