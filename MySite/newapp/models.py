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
    test_name = models.CharField(max_length=50)
    belong_prj = models.CharField(max_length=50)

    request = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    response = models.CharField(max_length=50)
    create_time = models.CharField(max_length=50)
    update_time = models.CharField(max_length=50)
