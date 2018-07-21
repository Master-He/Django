from django.db import models

# Create your models here.
from django.db.models import Manager


# 在users/models.py文件添加以下代码
class DepartmentManager(Manager):
    def all(self):
        """重写all方法：只返回没有删除的部门"""
        return super().all().filter(is_delete=False)

    def create_dep(self, name, create_date):
        """封装新增部门的方法，方便调用"""

        dep = Department()
        dep.name = name
        dep.create_date = create_date
        dep.save()
        return dep


class Department(models.Model):
    """部门类"""

    # 部门名称:字符串类型(必须指定最大长度)
    name = models.CharField(max_length=20)
    # 部门成立时间: 日期类型
    # auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间。
    # auto_now_add为添加时的时间，更新对象时不会有变动。
    create_date = models.DateField(auto_now_add=True)
    # 逻辑删除标识: 标识部门是否删除
    is_delete = models.BooleanField(default=False)

    objects = DepartmentManager()

    def __str__(self):
        return self.name

    class Meta:
        """指定表名"""
        db_table = 'department'
        verbose_name = '部门'
        verbose_name_plural = verbose_name  # 去掉复数的s


class Employee(models.Model):
    """员工类"""
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    # sex性别枚举类, 嵌套元组((0,'男'),(1,'女'))
    choices_gender = (
        (0, '男'),
        (1, '女'),
    )
    gender = models.IntegerField(default=0, choices=choices_gender)

    # 工资: 浮点类型(必须要指定两个选项,最大数字个数和小数位数)
    # max_digits
    # decimal_places
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    # 员工入职时间
    hire_date = models.DateField(auto_now_add=True)
    # 备注信息: 可以为空 null=True,blank=True
    comment = models.CharField(max_length=300, null=True, blank=True)

    # 一对多的外键: 员工所属部门 department_id
    department = models.ForeignKey('Department', on_delete=models.PROTECT)  # 注意是双引号的 'Department'

    def __str__(self):
        return self.name

    class Meta:
        # 指定表名
        db_table = "employee"
        verbose_name = '员工'
        verbose_name_plural = verbose_name  # 去掉复数的s


# 新增模型类和测试字段
class TestUser(models.Model):
    # 用户名
    name = models.CharField(max_length=20)
    # 用户头像
    # upload_to 指定该字段的图片保存在MEDIA_ROOT目录中的哪个子目录下
    # avatar = models.ImageField(upload_to='users', null=True)


if __name__ == '__main__':
    pass
