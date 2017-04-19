# -*- coding:utf-8 -*-
from django.conf.urls import url, include


from .views import UserInfoView, UploadImageView, UpdataPwdView


urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),

    # 用户信息
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),

    # 用户个人中心修改密码
    url(r'^update/pwd/$', UpdataPwdView.as_view(), name='update_pwd'),

]