from django.urls import path

from student.views import index

urlpatterns = [
    path('', index, name='index'),
]
