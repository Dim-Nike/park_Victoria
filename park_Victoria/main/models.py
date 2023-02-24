from django.db import models

# Create your models here.


class CategoriesProduct(models.Model):
    class Meta:
        verbose_name = 'Категория цветов'
        verbose_name_plural = 'Категории цветов'

    name = models.CharField(verbose_name='Наименование категории', max_length=100)
    photo = models.ImageField(verbose_name='Фотография', upload_to='photo/categoriesProducts/%Y/%m/%d/')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Цветы'
        verbose_name_plural = 'Цветы'

    name = models.CharField(verbose_name='Наименование продукта', max_length=155)
    categories = models.ForeignKey(CategoriesProduct, verbose_name='Категория', on_delete=models.PROTECT)
    photo = models.ImageField(verbose_name='Фотография', upload_to='photo/Products/%Y/%m/%d/')
    description = models.TextField(verbose_name='Краткое описание(300 символов)', max_length=300)
    price = models.IntegerField(verbose_name='Цена')
    is_active = models.BooleanField(verbose_name='Опубликованно')
    popular = models.BooleanField(verbose_name='Отображается на главной странице(может быть 3)')
    product_is_day = models.BooleanField(verbose_name='Продукт недели(может быть один)')


