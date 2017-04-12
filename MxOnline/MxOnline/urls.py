from django.conf import settings
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.static import serve #处理静态文件


import xadmin

from users.views import LoginView, RegisterView, ActiveUserView, ForgetView, ResetView, ModifyPwdView

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    # url(r'^login/$', TemplateView.as_view(template_name="login.html"), name="login"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    # 验证用户注册后，在邮件里点击注册链接
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url(r'^forget/$', ForgetView.as_view(), name='forget_pwd'),
    # 用户在邮件里点击重置密码链接
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),

    # 重置密码表单 POST 请求
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),
]

