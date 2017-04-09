from django.conf.urls import url, include
from django.contrib import admin
from message.views import getform

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 必须以 /$ 结尾，否则会使名字相似的 url 冲突
    url(r'^form/$', getform, name="go_form"),

    # url(r'^form', getform, name="go_form"),
    # url(r'^formtest', admin.site.urls),

]
