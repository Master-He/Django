import json

from django.http import HttpResponse
from django.http.response import JsonResponse, HttpResponseRedirect

from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from users.decorators import check_ip


def index(request):
    """访问首页的视图"""
    # return HttpResponse("<h2>hello django</h2>")
    print("index")

    context = {
        'name': 'django',
        'my_list': [1, 2, 3, 4],
        'my_dict': {
            'name': 'python',
            'age': 20,
            'gender': '男',
        }
    }
    # 方式一
    # render参数一:请求对象
    # render参数二:模块路径
    # render参数三:字典数据


    return render(request, 'users/index.html', context)

    # 方式二
    # # 获取模板对象
    # template = loader.get_template('users/index.html')  # type: Template
    # # 渲染得到字符串
    # html_str = template.render(context)
    # # 响应请求
    # return HttpResponse(html_str)


# 未命名参数(位置参数): 按定义的顺序传递
def news1(request, a, b):
    return HttpResponse("显示新闻: %s类%s页" % (a, b))


# 命名参数(关键字参数) : 按定义的组名传递
def news2(request, category, page):
    return HttpResponse("显示新闻: %s类%s页" % (category, page))


def news3(request):
    # ?category=1&apge=2&a=3&a=4
    category = request.GET.get('category')
    page = request.GET.get('page')
    a = request.GET.getlist('a')  # 一键多值通过getlist获取

    text = "显示新闻: %s类%s页 <br/> a = %s" % (category, page, a)

    return HttpResponse(text)


def news4(request):
    # post方法(表单)
    category = request.POST.get('category')
    page = request.POST.get('page')
    a = request.POST.getlist('a')

    text = "显示新闻news4: %s类%s页 <br/> a = %s" % (category, page, a)

    return HttpResponse(text)


def news5(request):
    #  获取json字符串
    json_str = request.body
    json_str = json_str.decode()  # bytes-->str

    # 解析json  # 导入json  import json  --> 字典转json: json_str json.dumps(dict_data)
    dict_data = json.loads(json_str)  # python3.6后可以省略bytes-->str这一步骤
    # dict_data = json.load() # 注意load和loads
    category = dict_data.get('category')
    page = dict_data.get('page')

    text = "获取body中的json数据 : category = %s, page = %s " % (category, page)
    return HttpResponse(text)


def news6(request):
    # 获取请求头属性值时，需要添加前缀 HTTP_ 并转成大写，作为键来获取值
    a = request.META.get("HTTP_A")
    b = request.META.get("HTTP_B")
    text = "请求头的数据 : a = %s, b = %s " % (a, b)

    return HttpResponse(text)


def news7(request):
    # user属性
    a = request.user
    print(a)  # 没人登录就是AnonymousUser

    print(type(a))  # <class 'django.utils.functional.SimpleLazyObject'>
    print(a.is_authenticated())  # 判断用户是否已经登录  # 没登录 False

    # 管理员怎么登录???

    return HttpResponse("success")


def resp(request):
    """普通响应"""
    response = HttpResponse(content="响应体", content_type="text/plain", status=201, )
    response["a"] = 1
    response["b"] = 2
    return response


def resp2(request):
    """json响应"""
    data = [{"name": "中文"}, {"speed": "90"}]
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def resp3(request):
    """重定向响应"""
    # return HttpResponseRedirect('/index')
    return redirect('/index')


def resp4(request):
    """reverse函数: 动态生成URL地址，解决url硬编码维护麻烦的问题"""
    my_url = reverse("users:index")
    print(my_url)
    return redirect(my_url)


def set_cookie(request):
    response = HttpResponse("设置cookie")
    response.set_cookie('a', '2', max_age=10)
    return response


def get_cookie(request):
    a = request.COOKIES.get('a')
    print(type(a))
    return HttpResponse(a)


def set_session(request):
    """生成session"""
    request.session['user_id'] = "he"
    request.session['user_name'] = "haha"
    return HttpResponse("设置session")


def get_session(request):
    """获取session"""
    a = request.session.get('user_id', "不存在")

    b = request.session.get('user_name', "不存在")
    c = request.session.get("no", "默认值")  # c得到的是默认值
    text = "user_id = %s , user_name = %s, c = %s" % (a, b, c)
    return HttpResponse(text)


def del_session(request):
    data = "删除成功"
    # try:
    #     del request.session['user_id']
    # except Exception as e:
    #     print("删除错误, 错误类型:", e)
    #     data = "删除错误, 错误类型" + str(e)

    request.session.clear()
    # request.session.flush()

    return HttpResponse(data)


@check_ip
def post(request):
    # 显示发帖界面
    return render(request, 'users/post.html')


def do_post(request):
    """执行发帖操作"""
    title = request.POST.get('title')
    content = request.POST.get('content')

    text = "title = %s , content = %s " % (title, content)
    return HttpResponse(text)


class CheckIpMixin(object):
    """扩展类:检测ip是否为黑名单"""

    # @method_decorator(check_ip)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# 方式三
# @method_decorator(check_ip,name='post')  # 为特定的请求方法添加
# @method_decorator(check_ip,name='get')  # 为特定的请求方法添加
# @method_decorator(check_ip,name='dispatch')  # 为所有的请求方法添加
class PostView(CheckIpMixin, View):
    # 方式二
    # 给所有的http方法都添加装饰其
    # 重写父类方法快捷键 ctrl + o
    # @method_decorator(check_ip)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)


    # @method_decorator(check_ip)  # 方式一
    def get(self, request):
        return render(request, 'users/post2.html')

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')

        text = "title = %s , content = %s " % (title, content)
        return HttpResponse(text)
