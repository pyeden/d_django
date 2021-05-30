from django.db import models


# Create your models here.

class Student(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (3, '未知'),
    ]

    STATUS_ITEMS = [
        (1, '申请'),
        (2, '通过'),
        (0, '拒绝'),
    ]

    name = models.CharField('姓名', max_length=255)
    sex = models.IntegerField('性别', choices=SEX_ITEMS, default=0)
    profession = models.CharField('职业', max_length=255)
    email = models.EmailField('邮箱', max_length=255)
    qq = models.CharField('QQ', max_length=255)
    phone = models.CharField('电话', max_length=255)
    status = models.IntegerField('审核状态', choices=STATUS_ITEMS, default=0)
    create_t = models.DateTimeField('创建时间', auto_now_add=True)
    update_t = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return f'student: {self.name}'

    class Meta:
        verbose_name = verbose_name_plural = '学生信息'
