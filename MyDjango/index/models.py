from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField('名称', max_length=50)
    weight = models.CharField('重量', max_length=20)
    describe = models.CharField('描述', max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = verbose_name
