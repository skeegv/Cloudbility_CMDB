from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout  # 用于用户检测,用户登录,退出
from django.contrib.auth.decorators import login_required  # 用于检测用户是否已登录




# 登录页
def login(request):
    error = ''
    if request.method == "POST":
        # 获取用户输入的 username and password
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 验证用户输入的 username and password
        user = authenticate(username=username, password=password)

        if user:
            # login将django user 对象写入到 Session.前端 通过 request.user 可以取到.(只要一登录 request.user 就自动封装到整个请求会话里了)
            login(request, user)
            # 登录成功后也要根据 next 来跳转,因为我们配置了Django 的用户认证 login_url(装饰器会自动帮我们获取上一次request.path 的记录并写在 next 参数里)
            return redirect(request.GET.get('next') or '/')
        else:
            error = "Wrong username or password!"

    return render(request, 'login.html', {'error': error})


# 首页
# @login_required(login_url='/login/')
# @login_required  # 在 settings.py 里我们已经写了 LOGIN_URl='/lognin/' 所以这里就不用写了
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

    return render(request, 'register.html')


def privacy(request):
    return render(request, 'privacy-policy.html')