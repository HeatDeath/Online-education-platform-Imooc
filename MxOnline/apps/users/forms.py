# -*- coding:utf-8 -*-
from django import forms


# 用于验证提交的表单，预处理表单
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

