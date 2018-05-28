# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json

from login import models

# Create your views here.


@require_http_methods(["GET"])
def login(request):
    username = ""
    pwd = ""
    if request.method == "GET":
        username = request.GET.get("username")
        pwd = request.GET.get("pwd")
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


@require_http_methods(["GET", "POST"])
def get_article_sort(request):
    response = dict()
    response["success"] = "true"
    sort = models.ArticleSort.objects.all()
    if len(sort) > 0:
        result = dict()
        result["status"] = "true"
        result["msg"] = "查询到分类信息"
        result["datas"] = json.loads(serializers.serialize("json", sort))
        response["data"] = result
    else:
        result = dict()
        result["status"] = "false"
        result["msg"] = "为查询到分类信息，请先建立文章分类"
        result["datas"] = "None"
        response["data"] = result
    return JsonResponse(response)


@require_http_methods(["GET"])
def get_articles(request):
    search_string = ""
    sort_id = ""
    if request.method == "GET":
        search_string = request.GET.get("search_string")
        if search_string is not None:
            print("string" + search_string)
        sort_id = request.GET.get("sort_id")
    response = dict()
    response["success"] = "true"
    articles = models.Article.objects.filter(sort=sort_id, title__contains=search_string)
    if len(articles) > 0:
        result = dict()
        result["status"] = "true"
        result["msg"] = "查询到相关文章"
        result["datas"] = json.loads(serializers.serialize("json", articles))
        response["data"] = result
    else:
        result = dict()
        result["status"] = "false"
        result["msg"] = "为查询到相关文章"
        result["datas"] = "None"
        response["data"] = result
    return JsonResponse(response)
