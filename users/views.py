import json

from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.


def index(request):
    """访问首页的视图"""
    # return HttpResponse("<h2>hello django</h2>")
    return render(request, 'users/index.html')


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
