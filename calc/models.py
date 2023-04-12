from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Введите категорию товаров', verbose_name='Категория товаров')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, help_text='Введите название продукта', verbose_name='Название продукта')
    serial_number = models.CharField(max_length=4, help_text='Введите серийный номер', verbose_name='Серийный номер')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, help_text='Введите категорию товара', verbose_name='Категория товара', null=True)
    vp = models.DecimalField(help_text='Введите VP', verbose_name='VP продукта', decimal_places=2, max_digits=5, null=True)
    proc100 = models.DecimalField(help_text='100', verbose_name='100', decimal_places=2, max_digits=8, null=True)
    proc50 = models.DecimalField(help_text='50', verbose_name='50', decimal_places=2, max_digits=8, null=True)
    proc42 = models.DecimalField(help_text='42', verbose_name='42', decimal_places=2, max_digits=8, null=True)
    proc35 = models.DecimalField(help_text='35', verbose_name='35', decimal_places=2, max_digits=8, null=True)
    proc25 = models.DecimalField(help_text='25', verbose_name='25', decimal_places=2, max_digits=8, null=True)
    proc15 = models.DecimalField(help_text='15', verbose_name='15', decimal_places=2, max_digits=8, null=True)

    def __str__(self):
        return self.name