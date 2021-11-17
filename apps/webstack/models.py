from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField("类别名称", max_length=10)
    icon = models.CharField('图标', max_length=20, default='linecons-lightbulb')

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self) -> str:
        return self.name

class SubCategory(models.Model):
    name = models.CharField("子类别名称", max_length=10)
    parent = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "子分类"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self) -> str:
        return self.name

class Site(models.Model):
    url = models.CharField('网站链接', max_length=256, default='#')
    logo_url = models.CharField('logo链接', max_length=256, default='')
    name = models.CharField('网站名称', max_length=20)
    describtion = models.TextField('网站简介', blank=True)
    is_show = models.BooleanField('是否展示', default=True)

    category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)

    class Meta:
        verbose_name = '站点'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self) -> str:
        return self.name

