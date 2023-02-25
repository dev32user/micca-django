from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    content = models.TextField(default='name', verbose_name='제품명')
    product_detail = models.TextField(default='',verbose_name='상세설명')
    price = models.IntegerField(default=0, verbose_name='가격')
    stock = models.IntegerField(default=0, verbose_name='재고')
    imgfile = models.ImageField(null=True, upload_to="", blank=True, verbose_name='이미지')

    class Meta:
        db_table = 'Shop_Product'
        verbose_name = '제품'
        verbose_name_plural = '제품'

    def __str__(self):
        return self.content


