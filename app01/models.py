from django.db import models


class User(models.Model):
    name = models.CharField(verbose_name='昵称', max_length=32)
    username = models.CharField(verbose_name='登录用户名', max_length=32, unique=True)
    password = models.CharField(verbose_name='登录密码', max_length=64)
    email = models.EmailField(verbose_name='邮箱')

    def __str__(self):
        return "%s-%s-%s" (self.name, self.username, self.email)

