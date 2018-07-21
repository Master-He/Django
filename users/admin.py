from django.contrib import admin

# Register your models here.

from users.models import Department, Employee, TestUser


class DepartmentStackedInline(admin.StackedInline):
    model = Employee  # 关联对象类型


class DepartmentTabularInline(admin.TabularInline):
    model = Employee  # 关联对象类型


class DepartmentAdmin(admin.ModelAdmin):
    # 指定要显示的属性
    list_display = ["id", 'name']
    # 隐藏顶部操作栏
    actions_on_top = False  # 默认False
    # 显示底部操作栏
    actions_on_bottom = True  # 默认True
    # 搜索部门名称
    search_fields = ['name']

    inlines = [DepartmentTabularInline]  # 栈的方式显示

    # inlines = [DepartmentStackedInline]      # 表格样式显示



class EmployeeAdmin(admin.ModelAdmin):
    # 指定要显示的属性
    list_display = ["id", "name", "gender", "age", "comment", "department"]
    list_per_page = 5

    # 显示过滤栏: 按性别和部门过滤
    list_filter = ['gender', 'department']

    # 指定是编辑表中的哪些字段
    # fields = ['name', "age", "department"]


    # 字段分组显示
    # fieldsets不能与fields同时使用
    fieldsets = (
        ('基本', {'fields': ('name', 'age', 'gender')}),
        ('高级', {'fields': ('comment', 'department')}),
    )

    class Meta:
        verbose_name = '员工'
        # verbose_name_plural = verbose_name  # 去掉复数的s


# 注册Model类
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(TestUser)


admin.site.site_title = '传智OA'
admin.site.site_header = '传智OA系统'
admin.site.index_title = '欢迎使用传智OA'
