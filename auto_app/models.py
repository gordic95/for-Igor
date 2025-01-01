from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator
from django.db import models


class AutoBrand(models.Model):
    name = models.CharField(max_length=50, verbose_name='Марка')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

class AutoModel(models.Model):
    name_model = models.CharField(max_length=50, verbose_name='Модель')


    def __str__(self):
        return self.name_model

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

class AutoTechCHar(models.Model):
    power = models.PositiveIntegerField(validators=[MaxValueValidator(2000)], verbose_name='Мощность')
    color = models.CharField(max_length=10, verbose_name='Цвет')
    brand = models.ForeignKey(AutoBrand, on_delete=models.CASCADE, verbose_name='Марка')
    model = models.ForeignKey(AutoModel, on_delete=models.CASCADE, verbose_name='Модель')
    vin = models.CharField(unique=True, max_length=17, verbose_name='VIN')
    year = models.PositiveIntegerField(validators=[MinValueValidator(1800)], verbose_name='Год')
    car_milage = models.PositiveIntegerField(validators=[MaxValueValidator(600000)], verbose_name='Пробег')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey('AutoCategory', on_delete=models.CASCADE, verbose_name='Категория', blank=True, null=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, verbose_name='Профиль', blank=True, null=True)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', default='images/1.webp')


    def __str__(self):
        return f'{self.brand} {self.model}'

    class Meta:
        verbose_name = 'Технические характеристики'
        verbose_name_plural = 'Технические характеристики'


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    profile_name = models.CharField(max_length=50, verbose_name='Никнэйм')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')
    email = models.EmailField(max_length=50, verbose_name='Email')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateField(auto_now=True, verbose_name='Дата обновления')


    def __str__(self):
        return self.profile_name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class AutoCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
