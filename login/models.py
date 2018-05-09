from django.db import models

# Create your models here.


class UserType(models.Model):
    '''
    用户类型表
    '''
    typename = models.CharField(max_length=32)


class UserInfo(models.Model):
    '''
    用户信息表
    '''
    username = models.CharField(max_length=20)
    authstr = models.CharField(max_length=32)
    usertype = models.ForeignKey(UserType, on_delete=models.CASCADE)


class ArticleSort(models.Model):
    '''
    文章分类类别表
    '''
    name = models.CharField(max_length=50)


class Article(models.Model):
    '''
    文章内容表
    '''
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    createtime = models.DateTimeField
    sort = models.ForeignKey(ArticleSort, on_delete=models.CASCADE)
    cover = models.CharField(max_length=200)
    summary = models.TextField
    content = models.TextField
    recommend = models.IntegerField
    display = models.IntegerField
    watch = models.IntegerField


class DataInfo(models.Model):
    '''
    跟踪数据表
    '''
    ip = models.IPAddressField
    time = models.DateTimeField
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)


class BannerInfo(models.Model):
    '''
    Banner信息表
    '''
    imagepath = models.CharField(max_length=200)
    createtime = models.DateTimeField


class BlogInfo(models.Model):
    '''
    博客基本信息表
    '''
    name = models.CharField(max_length=200)
    logopath = models.CharField(max_length=200)
    description = models.TextField
    introduce = models.TextField
