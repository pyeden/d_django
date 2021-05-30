from django.urls import path

from student.views import IndexView

app_name = 'student'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
