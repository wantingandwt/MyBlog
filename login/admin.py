from django.contrib import admin
from login import models


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("username", "authstr", "usertype")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "createtime", "sort", "cover", "summary",
                    "content", "recommend", "display", "watch")


class BannerInfoAdmin(admin.ModelAdmin):
    list_display = ("imagepath", "createtime")


class BlogInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "logopath", "description", "introduce")


class DataInfoAdmin(admin.ModelAdmin):
    list_display = ("ip", "time", "article_id")


# Register your models here.
admin.site.register(models.UserType)
admin.site.register(models.UserInfo, UserInfoAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.ArticleSort)
admin.site.register(models.BannerInfo, BannerInfoAdmin)
admin.site.register(models.BlogInfo, BlogInfoAdmin)
admin.site.register(models.DataInfo, DataInfoAdmin)
