from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View



from .models import UserProfile
from .forms import LoginForm
# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 用 Q 实现并集查询
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            password = request.POST.get("password", "")
            # 使用 authenticate() 方法进行验证
            user = authenticate(username=user_name, password=password)
            # 当符合验证的时候，不返回 None
            if user is not None:
                # 使用 login() 方法进行登录
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误", "login_form": login_form})

# 用户登录
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        # 验证 POST 的每个参数是否合法
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            # 使用 authenticate() 方法进行验证
            user = authenticate(username=user_name, password=password)

            if user is not None:
                # 使用 login() 方法进行登录
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, 'login.html', {'msg': '用户名或者密码错误！'})
        else:
            return render(request, 'login.html', {"login_form": login_form})








# --------------------------------------------------------------------
# 定义一个名为 LoginView 并继承 View 的 class 替代 user_login() 方法
# def user_login(request):
#     if request.method == "POST":
#         user_name = request.POST.get("username", "")
#         password = request.POST.get("password", "")
#         # 使用 authenticate() 方法进行验证
#         user = authenticate(username=user_name, password=password)
#         # 当符合验证的时候，不返回 None
#         if user is not None:
#             # 使用 login() 方法进行登录
#             login(request, user)
#             return render(request, "index.html")
#         else:
#             return render(request, "login.html", {"msg": "用户名或密码错误"})
#     elif request.method == "GET":
#         return render(request, "login.html", {})
# --------------------------------------------------------------------

