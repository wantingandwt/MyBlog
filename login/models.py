# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Create your models here.


class UserType(models.Model):
    '''
    用户类型表
    '''
    def __str__(self):
        return self.typename

    typename = models.CharField(max_length=32)


class UserInfo(models.Model):
    '''
    用户信息表
    '''
    def __str__(self):
        return self.username

    username = models.CharField(max_length=20)
    authstr = models.CharField(max_length=32)
    usertype = models.ForeignKey(UserType, on_delete=models.CASCADE)


class ArticleSort(models.Model):
    '''
    文章分类类别表
    '''
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)


class Article(models.Model):
    '''
    文章内容表
    '''
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    createtime = models.DateTimeField(default=timezone.now, null=True)
    sort = models.ForeignKey(ArticleSort, on_delete=models.CASCADE)
    cover = models.CharField(max_length=200)    # 封面图路径
    summary = models.TextField(null=True)      # 概要
    content = models.TextField(null=True)
    recommend = models.IntegerField(default=0)     # 是否推荐
    display = models.IntegerField(default=1)
    watch = models.IntegerField(default=0)


class DataInfo(models.Model):
    '''
    跟踪数据表
    '''
    def __str__(self):
        return self.ip

    ip = models.GenericIPAddressField(protocol="IPv4", null=True)
    time = models.DateTimeField(default=timezone.now, null=True)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)


class BannerInfo(models.Model):
    '''
    Banner信息表
    '''
    imagepath = models.CharField(max_length=200)
    createtime = models.DateTimeField(default=timezone.now, null=True)


class BlogInfo(models.Model):
    '''
    博客基本信息表
    '''
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    logopath = models.CharField(max_length=200)
    description = models.TextField(null=True)
    introduce = models.TextField(null=True)
