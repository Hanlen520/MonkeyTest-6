# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


class ProjectInfo(models.Model):
    project_name = models.CharField(max_length=30)
    responsible_name = models.CharField(max_length=30)
    test_user = models.CharField(max_length=30)
    dev_user = models.CharField(max_length=30)
    publish_app = models.CharField(max_length=30)
    simple_desc = models.CharField(max_length=100)
    other_desc = models.CharField(max_length=100)
    create_time = models.CharField(max_length=50)

class TestInfo(models.Model):
    test_name = models.CharField('用例名称', max_length=50)
    belong_project = models.CharField('所属项目', max_length=50)

    request = models.TextField('请求信息')
    author = models.CharField('编写人员',max_length=50)
    remark = models.CharField('其他信息', max_length=100)
    response = models.TextField('返回信息',max_length=50)
    create_time = models.CharField(max_length=50)
    update_time = models.CharField(max_length=50)

    # class Meta:
    #     verbose_name = '用例信息'
    #     db_table = 'TestCaseInfo'
    #
    # type = models.IntegerField('test/config', default=1)
    # name = models.CharField('用例/配置名称', max_length=50)
    # belong_project = models.CharField('所属项目', max_length=50)
    # belong_module = models.ForeignKey(ModuleInfo, on_delete=models.CASCADE)
    # include = models.CharField('包含config/test', max_length=400, null=True)
    # author = models.CharField('编写人员', max_length=20)
    # request = models.TextField('请求信息')

class EnvInfo(models.Model):
    env_name = models.TextField('环境名称')
    base_url = models.CharField('地址',max_length=50)
    env_key = models.TextField('环境key',max_length=50)
    simple_desc = models.CharField('简要说明', max_length=100)
    create_time = models.CharField(max_length=50)
    update_time = models.CharField(max_length=50)
