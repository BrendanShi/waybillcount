#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 16:29
# @Author  : 石小磊@樱桃林

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.



class Account(models.Model):
    """
    个人账户
    """
    ROLE = (
        ("manager","管理员"),
        ("picker","接单员"),
        ("driver","司机")
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='account')
    role = models.CharField("角色",max_length=20,choices=ROLE)


    class Meta:
        verbose_name = '账号管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.get_role_display()
