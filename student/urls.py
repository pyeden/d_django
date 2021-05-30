from django.urls import path

from student.views import index

app_name = 'student'

urlpatterns = [
    path('', index, name='index'),
]
