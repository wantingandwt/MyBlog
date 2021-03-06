# Generated by Django 2.0.2 on 2018-05-30 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180508_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='c_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='display',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='article',
            name='recommend',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='watch',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bannerinfo',
            name='c_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='introduce',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='datainfo',
            name='ip',
            field=models.GenericIPAddressField(null=True, protocol='IPv4'),
        ),
        migrations.AddField(
            model_name='datainfo',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
