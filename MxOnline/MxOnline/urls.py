# -*- coding:utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.static import serve #处理静态文件


import xadmin


from users.views import LoginView, RegisterView, ActiveUserView, \
                        ForgetView, ResetView, ModifyPwdView, LogoutView, IndexView
from organization.views import OrgView
from MxOnline.settings import MEDIA_ROOT
# from MxOnline.settings import STATIC_ROOT


urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    # url(r'^login/$', TemplateView.as_view(template_name="login.html"), name="login"),
    url(r'^login/$', LoginView.as_view(), name="login"),

    url(r'^logout/$', LogoutView.as_view(), name="logout"),

    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    # 验证用户注册后，在邮件里点击注册链接
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url(r'^forget/$', ForgetView.as_view(), name='forget_pwd'),
    # 用户在邮件里点击重置密码链接
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),

    # 重置密码表单 POST 请求
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),

    # 课程机构 url 配置
    url(r'^org/', include('organization.urls', namespace='org')),


    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),

    # 课程相关 url 配置
    url(r'^course/', include('courses.urls', namespace='course')),

    # 教师相关 url 配置
    url(r'^teacher/', include('organization.urls', namespace='teacher')),

    # 用户相关 url 配置
    url(r'^users/', include('users.urls', namespace='users')),

    # # 富文本相关 Url
    # url(r'^ueditor/',include('DjangoUeditor.urls'))

]

# 全局 404 页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'


