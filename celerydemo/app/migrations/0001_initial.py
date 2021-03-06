# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvPool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advcode', models.CharField(db_index=True, max_length=50, verbose_name='\u5e7f\u544a')),
                ('amount', models.IntegerField(default=0, verbose_name='\u9700\u6c42\u6570\u91cf')),
                ('logourl', models.CharField(default='', max_length=250, verbose_name='logo')),
                ('index', models.IntegerField(db_index=True, default=0, verbose_name='\u9875\u7801')),
                ('request_id', models.CharField(max_length=20, verbose_name='\u8bf7\u6c42ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('complete_amount', models.IntegerField(default=0, verbose_name='\u9700\u6c42\u6570\u91cf')),
                ('complete_status', models.BooleanField(choices=[(0, '\u5426'), (1, '\u662f')], default=False, verbose_name='\u5df2\u5b8c\u6210')),
            ],
            options={
                'verbose_name': '\u5e7f\u544a',
                'db_table': 'cuntao_advpool',
                'managed': True,
                'verbose_name_plural': '\u5e7f\u544a',
            },
        ),
        migrations.CreateModel(
            name='CodePool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=20, verbose_name='\u7f16\u7801')),
                ('index', models.IntegerField(db_index=True, default=0, verbose_name='\u9875\u7801')),
                ('request_id', models.CharField(max_length=20, verbose_name='\u8bf7\u6c42ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('status', models.BooleanField(choices=[(0, '\u5426'), (1, '\u662f')], db_index=True, default=False, verbose_name='\u5173\u8054\u72b6\u6001')),
            ],
            options={
                'verbose_name': '\u7f16\u7801',
                'db_table': 'cuntao_codepool',
                'managed': True,
                'verbose_name_plural': '\u7f16\u7801',
            },
        ),
        migrations.CreateModel(
            name='PackageAmountConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_amount', models.IntegerField(default=0, verbose_name='\u5305\u88f9\u57fa\u7840\u6570\u91cf')),
                ('index', models.IntegerField(db_index=True, default=0, verbose_name='\u9875\u7801')),
                ('request_id', models.CharField(max_length=20, verbose_name='\u8bf7\u6c42ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5305\u88f9\u57fa\u7840\u6570\u91cf',
                'db_table': 'cuntao_packageamountconfig',
                'managed': True,
                'verbose_name_plural': '\u5305\u88f9\u57fa\u7840\u6570\u91cf',
            },
        ),
        migrations.CreateModel(
            name='PackageCodePool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packagecode', models.CharField(db_index=True, max_length=20, verbose_name='\u5305\u88f9\u7801')),
                ('index', models.IntegerField(db_index=True, default=0, verbose_name='\u9875\u7801')),
                ('request_id', models.CharField(max_length=20, verbose_name='\u8bf7\u6c42ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5305\u88f9\u7801',
                'db_table': 'cuntao_packagecodepool',
                'managed': True,
                'verbose_name_plural': '\u5305\u88f9\u7801',
            },
        ),
        migrations.CreateModel(
            name='SecurityCodePool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('securitycode', models.CharField(db_index=True, max_length=100, verbose_name='\u5bc6\u7801')),
                ('code', models.CharField(db_index=True, max_length=20, verbose_name='\u7f16\u7801')),
                ('code_prefix', models.CharField(db_index=True, default='', max_length=50, verbose_name='\u7f16\u7801\u524d\u7f00')),
                ('packagecode', models.CharField(blank=True, db_index=True, max_length=20, null=True, verbose_name='\u5305\u88f9\u7801')),
                ('card_adv', models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='\u5e7f\u544a')),
                ('sequence_first', models.BooleanField(default=False, verbose_name='\u662f\u5426\u4e3a\u5f00\u59cb\u53f7')),
                ('sequence_end', models.BooleanField(default=False, verbose_name='\u662f\u5426\u4e3a\u7ed3\u675f\u53f7')),
                ('index', models.IntegerField(db_index=True, default=0, verbose_name='\u9875\u7801')),
                ('request_id', models.CharField(max_length=20, verbose_name='\u8bf7\u6c42ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('complete_status', models.BooleanField(choices=[(0, '\u5426'), (1, '\u662f')], default=False, verbose_name='\u5df2\u5b8c\u6210')),
                ('importto_task_status', models.BooleanField(choices=[(0, '\u5426'), (1, '\u662f')], db_index=True, default=False, verbose_name='\u5df2\u5165\u5e93')),
                ('importto_task_batchno', models.CharField(db_index=True, max_length=20, verbose_name='\u5165\u5e93\u6279\u6b21\u53f7')),
                ('goods_send', models.BooleanField(choices=[(0, '\u5426'), (1, '\u662f')], db_index=True, default=False, verbose_name='\u53d1\u8d27\u6807\u5fd7')),
                ('goods_send_time', models.DateTimeField(blank=True, null=True, verbose_name='\u53d1\u8d27\u65f6\u95f4')),
                ('complete_retry_count', models.IntegerField(default=0)),
                ('cancel_status', models.BooleanField(choices=[(0, '\u5426'), (1, '\u662f')], db_index=True, default=False, verbose_name='\u5df2\u4f5c\u5e9f')),
            ],
            options={
                'verbose_name': '\u5bc6\u7801',
                'db_table': 'cuntao_securitycodepool',
                'managed': True,
                'verbose_name_plural': '\u5bc6\u7801',
            },
        ),
    ]
