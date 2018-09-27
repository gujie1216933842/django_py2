# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

from .tasks import cus_task


def index(request):
    cus_task.delay()
    return HttpResponse("Test async task")


