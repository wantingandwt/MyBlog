# Generated by Django 2.0.2 on 2018-05-08 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='usertype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.UserType'),
        ),
    ]
