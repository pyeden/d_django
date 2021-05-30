import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):

    def process_request(self, request):
        self.start_time = time.time()
        return

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        if request.path != reverse('student:index'):
            return None

        start = time.time()
        # 这种调用不会触发process_exception方法
        response = view_func(request)
        t = time.time() - start
        print(f'请求方式：{request.method}, 视图函数：{view_func.__name__} 执行时间：{t} 秒')
        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        t = time.time() - self.start_time
        print(f'请求方式：{request.method}, api：{request.path} 请求处理时间：{t} 秒')
        return response
