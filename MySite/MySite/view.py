#!/user/bin/env python
# -*- coding:utf-8 -*-

from django.http import HttpResponse

#
# def hello(request):
#     return HttpResponse("Hello world ! ")
# if __name__ == '__main__':
#     pass

from django.shortcuts import render


def hello(request):
    context = {}
    # context['hello'] = 'Hello World!'
    return render(request, 'mysite.html', context)