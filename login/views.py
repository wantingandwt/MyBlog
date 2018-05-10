# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json

from login import models

# Create your views here.


@require_http_methods(["GET", "POST"])
def login(request):
    username = ""
    pwd = ""
    if request.method == "GET":
        username = request.GET.get("username")
        pwd = request.GET.get("pwd")
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
    response = dict()
    response["success"] = "true"
    user = models.UserInfo.objects.filter(username=username, authstr=pwd)
    # response["data"] = json.loads(serializers.serialize("json", user))
    if len(user) > 0:
        result = dict()
        result["status"] = "true"
        result["msg"] = "账号密码正确，验证成功"
        response["data"] = result
    else:
        result = dict()
        result["status"] = "false"
        result["msg"] = "账号密码不正确，验证失败"
        response["data"] = result
    return JsonResponse(response)
