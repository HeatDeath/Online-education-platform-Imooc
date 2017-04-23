import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from django.contrib.auth.models import User


from .models import EmailVerifyRecord, Banner, UserProfile


# class UserProfileAdmin(UserAdmin):
#     pass


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "暮雪后台管理系统"
    site_footer = "暮雪在线网"
    menu_style = "accordion"


# class UserProfileAdmin(object):
#     pass


class EmailVerifyRecordAdmin(object):

    list_display = ['code', 'email', 'send_type', 'send_time']  #后台自定义显示列
    search_fields = ['code', 'email', 'send_type'] #定义后台搜索
    list_filter = ['code', 'email', 'send_type', 'send_time'] #通过时间搜索
    model_icon = 'fa fa-rocket'
    # list_display = ('code',)


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time'] #后台自定义显示列 显示字段
    search_fields = ['title', 'image', 'url', 'index'] #定义后台搜索 搜索功能
    list_filter = ['title', 'image', 'url', 'index', 'add_time'] #过滤器 通过时间搜索
    model_icon = 'fa fa-rocket'

# 卸载原有的 User
# xadmin.site.unregister(User)
# xadmin.site.register(UserProfile, UserProfileAdmin)

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

