from django.conf import settings
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.static import serve #处理静态文件


import xadmin

from users.views import LoginView

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    # url(r'^login/$', TemplateView.as_view(template_name="login.html"), name="login"),
    url(r'^login/$', LoginView.as_view(), name="login")
]

