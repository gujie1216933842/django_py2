# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
bool_status_choices = (
    (0, '否'),
    (1, '是')
)


class SecurityCodePool(models.Model):
    securitycode = models.CharField('密码', max_length=100, db_index=True)
    code = models.CharField('编码', max_length=20, db_index=True)
    code_prefix = models.CharField('编码前缀', max_length=50, default='', db_index=True)
    packagecode = models.CharField('包裹码', max_length=20, null=True, blank=True, db_index=True)
    card_adv = models.CharField('广告', max_length=50, null=True, blank=True, db_index=True)
    sequence_first = models.BooleanField('是否为开始号', default=False)
    sequence_end = models.BooleanField('是否为结束号', default=False)
    index = models.IntegerField('页码', default=0, db_index=True)
    request_id = models.CharField('请求ID', max_length=20)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)
    complete_status = models.BooleanField('已完成', choices=bool_status_choices, default=False)
    importto_task_status = models.BooleanField('已入库', choices=bool_status_choices, default=False, db_index=True)
    importto_task_batchno = models.CharField('入库批次号', max_length=20, blank=False, null=False, db_index=True)
    goods_send = models.BooleanField('发货标志', choices=bool_status_choices, default=False, db_index=True)
    goods_send_time = models.DateTimeField('发货时间', blank=True, null=True)
    complete_retry_count = models.IntegerField(default=0)
    cancel_status = models.BooleanField('已作废', choices=bool_status_choices, default=False, db_index=True)

    class Meta:
        managed = True
        db_table = 'cuntao_securitycodepool'
        verbose_name = "密码"
        verbose_name_plural = "密码"

    def __unicode__(self):
        return self.securitycode  # 一定要返回字符串类型，否则django custom action操作过程里会报错


class CodePool(models.Model):
    code = models.CharField('编码', max_length=20, db_index=True)
    index = models.IntegerField('页码', default=0, db_index=True)
    request_id = models.CharField('请求ID', max_length=20)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    status = models.BooleanField('关联状态', choices=bool_status_choices, default=False,db_index=True)

    class Meta:
        managed = True
        db_table = 'cuntao_codepool'
        verbose_name = "编码"
        verbose_name_plural = "编码"

    def __unicode__(self):
        return self.code  # 一定要返回字符串类型，否则django custom action操作过程里会报错


class PackageCodePool(models.Model):
    packagecode = models.CharField('包裹码', max_length=20, db_index=True)
    index = models.IntegerField('页码', default=0, db_index=True)
    request_id = models.CharField('请求ID', max_length=20)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cuntao_packagecodepool'
        verbose_name = "包裹码"
        verbose_name_plural = "包裹码"

    def __unicode__(self):
        return self.packagecode  # 一定要返回字符串类型，否则django custom action操作过程里会报错


class AdvPool(models.Model):
    advcode = models.CharField('广告', max_length=50, db_index=True)
    amount = models.IntegerField('需求数量', default=0)
    logourl = models.CharField('logo', max_length=250, default='')
    index = models.IntegerField('页码', default=0, db_index=True)
    request_id = models.CharField('请求ID', max_length=20)
    create_time = models.DateTimeField('创建时间', blank=True, null=True, auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)
    complete_amount = models.IntegerField('需求数量', default=0)
    complete_status = models.BooleanField('已完成', choices=bool_status_choices, default=False)

    class Meta:
        managed = True
        db_table = 'cuntao_advpool'
        verbose_name = "广告"
        verbose_name_plural = "广告"

    def __unicode__(self):
        return self.advcode  # 一定要返回字符串类型，否则django custom action操作过程里会报错


class PackageAmountConfig(models.Model):
    package_amount = models.IntegerField('包裹基础数量', default=0)
    index = models.IntegerField('页码', default=0, db_index=True)
    request_id = models.CharField('请求ID', max_length=20)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'cuntao_packageamountconfig'
        verbose_name = "包裹基础数量"
        verbose_name_plural = "包裹基础数量"

    def __unicode__(self):
        return str(self.package_amount)  # 一定要返回字符串类型，否则django custom action操作过程里会报错

