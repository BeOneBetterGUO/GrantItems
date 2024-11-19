from django.db import models
from django.template.context_processors import request


class ItemCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='物品类别')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '物品类别'
        verbose_name_plural = verbose_name

class ItemStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name='物品状态')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '物品状态'
        verbose_name_plural = verbose_name

class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='物品名称')
    count = models.IntegerField(verbose_name='数量')
    type = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, verbose_name='物品类别')
    status = models.ForeignKey(ItemStatus, on_delete=models.CASCADE, verbose_name='物品状态')
    # 0:正常 1:预购 2:待出 3:已出
    is_consumable = models.BooleanField(verbose_name='是否消耗品',default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格',blank=True)
    image = models.ImageField(upload_to='items/', verbose_name='图片',blank=True,default='static/images/logo.png')
    overdue = models.DateField(verbose_name='过期时间',blank=True,null=True)
    link = models.URLField(verbose_name='链接',blank=True)
    description = models.TextField(verbose_name='描述',blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='所有者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '物品'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']