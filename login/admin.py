from django.contrib import admin
from login import models

# Register your models here.
admin.site.register(models.UserType)
admin.site.register(models.UserInfo)
admin.site.register(models.Article)
admin.site.register(models.ArticleSort)
admin.site.register(models.BannerInfo)
admin.site.register(models.BlogInfo)
admin.site.register(models.DataInfo)
