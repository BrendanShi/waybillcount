#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 16:29
# @Author  : 石小磊@樱桃林

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
