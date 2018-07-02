# -*- coding: utf-8 -*-
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import os

from login import models

# Create your views here.


@require_http_methods(["POST"])
def login(request):
    username = ""
    pwd = ""
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


@require_http_methods(["POST"])
def do_article(request):
    response = dict()
    article = models.Article
    article.title = request.POST.get("title")
    article.author = request.POST.get("author")
    if request.POST.get("sort") is not None:
        article.sort = int(request.POST.get("sort"))
    else:
        article.sort = request.POST.get("sort")
    article.summary = request.POST.get("summary")
    article.content = request.POST.get("content")
    if request.POST.get("recommend") == "false":
        article.recommend = 0
    elif request.POST.get("recommend") == "true":
        article.recommend = 1
    if request.POST.get("display") == "false":
        article.display = 0
    elif request.POST.get("display") == "true":
        article.display = 1
    article.cover = request.POST.get("cover")

    ret_info = models.Article.objects.update_or_create(
        title=article.title,
        author=article.author,
        sort_id=article.sort,
        summary=article.summary,
        content=article.content,
        recommend=article.recommend,
        display=article.display,
        cover=article.cover,
    )

    response["success"] = "true"
    if ret_info[1]:
        result = dict()
        result["status"] = "true"
        result["msg"] = "新增成功"
        response["data"] = result
    else:
        result = dict()
        result["status"] = "false"
        result["msg"] = "新增失败"
        response["data"] = result
    return JsonResponse(response)


@require_http_methods(["GET"])
def watch_article(request):
    response = dict()
    response["success"] = "true"
    try:
        article_id = int(request.GET.get("a_id"))
        watch_set = models.Article.objects.filter(id=article_id).values("watch")
        watch = watch_set[0]["watch"]
        watch = watch + 1
        ret_info = models.Article.objects.filter(id=article_id).update(watch=watch)
        response["data"] = ret_info
        result = dict()
        result["status"] = "true"
        result["msg"] = "浏览量增加成功"
        result["watch"] = ret_info
        response["data"] = result
    except Exception:
        result = dict()
        result["status"] = "false"
        result["msg"] = "浏览量增加失败"
        response["data"] = result
    return JsonResponse(response)


@require_http_methods(["POST"])
def get_upload_file(request):
    if request.FILES.get("upfile") is not None:
        upload_file = request.FILES.get("upfile")
        file_path = "static/"
        file_path_name = file_path + upload_file.name
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        with open(file_path_name, "wb") as file:
            for i in upload_file.chunks():
                file.write(i)
        response = dict()
        response["filename"] = file_path_name
        return JsonResponse(response)

