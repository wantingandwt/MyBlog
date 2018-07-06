"""Myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from login import views


urlpatterns = [
    path('admin', admin.site.urls),
    path('login', views.login),
    path('get_article_sort', views.get_article_sort),
    path('get_articles', views.get_articles),
    path('do_article', views.do_article),
    path('watch_article', views.watch_article),
    path('get_upload_file', views.get_upload_file),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_URL}),
    path('del_article', views.del_article),
]
