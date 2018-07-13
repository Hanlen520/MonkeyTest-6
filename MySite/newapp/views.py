# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import  HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

import models
from httprunner import HttpRunner
from django.shortcuts import render_to_response
import io
import time
import yaml
import os
import json
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.
def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")

def add(request):
    a = request.GET['a']
    b = request.GET['b']

    return HttpResponse(str(int(a)+int(b)))

def add2(request,a,b):
    return HttpResponse(str(int(a) + int(b)))

def home(request):
    return render(request,'home.html')

def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )

def nav(request):
    studylist = [u'接口测试',u'Monkey脚本']
    info_dict ={'接口':'http','Monkey':'adb'}
    return render(request,'nav.html',{'studylist':studylist,'info_dict':info_dict})

def httpTest(request):
    return render(request,'httpTest.html')

def edit_case(request):
    return render(request,'edit_case.html')

def gobindex(request):
    return render(request,'bindex.html')

def testlist(request):
    return render(request, 'testlist.html')

def jsontest(request):
    return render(request, 'json.html')

def aceTest(request):
    return render(request, 'aceTest.html')

def addcase(request):
    projectlists = models.ProjectInfo.objects.all().values(
        'id', 'project_name', 'responsible_name', 'test_user', 'dev_user', 'publish_app', 'simple_desc', 'other_desc',
        'create_time')
    return render(request, 'addcase.html',{'projectlist':projectlists})

def addproject(request):
    return render(request,'addproject.html')

def test(request):
    projectlists = models.ProjectInfo.objects.all().values(
        'id', 'project_name', 'responsible_name', 'test_user', 'dev_user', 'publish_app', 'simple_desc', 'other_desc',
        'create_time')
    # projectlists = models.ProjectInfo.objects.all().values('id')
    paginator = Paginator(projectlists, 3)  # Show 25 contacts per page

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        projectlist = paginator.page(page)
    except (EmptyPage, InvalidPage):
        projectlist = paginator.page(paginator.num_pages)

    return render_to_response('testcasetry.html', {"projectlist": projectlist})
    # return render(request, 'testcasetry.html')

@csrf_exempt
def add_project(request):
    try:
        project_info = json.loads(request.body.decode('utf-8'))
    except ValueError:
        return HttpResponse('项目信息新增异常')

    project_name = project_info['project_name']
    responsible_name = project_info['responsible_name']
    test_user = project_info['test_user']
    dev_user = project_info['dev_user']
    publish_app = project_info['publish_app']
    simple_desc = project_info['simple_desc']
    other_desc = project_info['other_desc']

    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    # 表中插入数据
    models.ProjectInfo.objects.create(
        project_name=project_name,
        responsible_name=responsible_name,
        test_user=test_user,
        dev_user=dev_user,
        publish_app=publish_app,
        simple_desc=simple_desc,
        other_desc=other_desc,
        create_time=create_time
    )
    return HttpResponse('OK')

@csrf_exempt
def project_list(request):
    if ''!= request.body:
        str = json.loads(request.body.decode('utf-8'))
    projectlists = models.ProjectInfo.objects.all().values(
        'id', 'project_name', 'responsible_name', 'test_user', 'dev_user', 'publish_app', 'simple_desc', 'other_desc',
        'create_time')
    paginator = Paginator(projectlists, 10)  # Show 10 contacts per page

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        projectlist = paginator.page(page)
    except (EmptyPage, InvalidPage):
        projectlist = paginator.page(paginator.num_pages)
    return render(request, 'projectlist.html',{'projectlist':projectlist})

@csrf_exempt
def runcase(request):
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H-%M-%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s-%03d" % (data_head, data_secs)

    kwargs = {
        "failfast": False,
    }
    runner = HttpRunner(**kwargs)

    testcase_dir_path = os.path.join(os.getcwd(), "suite")
    testcase_dir_path = os.path.join(testcase_dir_path, time_stamp)
    if not os.path.exists(testcase_dir_path):
        os.mkdir(testcase_dir_path)

    url = request.POST['url']
    method = request.POST['method']
    base_url = request.POST['base_url']

    config = {
        'config': {
            'name': 'base_url config',
            'request': {
                'base_url':base_url
            }
        }
    }
    testcase_list = []

    testcase_list.append(config)
    req={'method':method,'url':url}
    req1={'name':'find','request':req}

    testcase_list.append({'test':req1})

    file_path=os.path.join(testcase_dir_path, "find.yml")
    with io.open(file_path, 'w', encoding='utf-8') as stream:
        yaml.dump(testcase_list, stream, indent=4, default_flow_style=False, encoding='utf-8')

    runner.run(testcase_dir_path)

    return render_to_response('report_template.html', runner.summary)