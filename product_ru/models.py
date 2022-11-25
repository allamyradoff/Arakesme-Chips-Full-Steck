from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True,
                            null=True, verbose_name='Имя')
    icon = models.FileField(upload_to='icon/', blank=True,
                            null=True, verbose_name='значок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    image = models.ImageField(upload_to='product/',
                              blank=True, null=True, verbose_name='Фото')
    image_2 = models.ImageField(upload_to='product/',
                                blank=True, null=True, verbose_name='Фото_2')
    image_3 = models.ImageField(upload_to='product/',
                                blank=True, null=True, verbose_name='Фото_3')
    desc = models.TextField(blank=True, null=True, verbose_name='Описание')

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 blank=True, null=True, verbose_name='К какой категории относится?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "продукты"


class Banner(models.Model):
    name = models.CharField(max_length=50, blank=True,
                            null=True, verbose_name='Имя')
    title = models.CharField(max_length=50, blank=True,
                             null=True,  verbose_name='Описание')
    big_image = models.ImageField(
        upload_to='banner/',
        max_length=None,
        blank=True,
        null=True,
        verbose_name='Фото сзади'
    )
    main_image = models.ImageField(upload_to='banner/',
                                   blank=True,
                                   null=True,
                                   verbose_name='Основное изображение'
                                   )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='В какому продукту он принадлежит'
    )

    name_2 = models.CharField(max_length=50, blank=True,
                              null=True, verbose_name='Имя')
    title_2 = models.CharField(max_length=50, blank=True,
                               null=True,  verbose_name='Описание')
    big_image_2 = models.ImageField(
        upload_to='banner/', max_length=None,
        blank=True,
        null=True,
        verbose_name='Фото сзади'
    )
    main_image_2 = models.ImageField(upload_to='banner/',
                                     blank=True,
                                     null=True,
                                     verbose_name='Основное изображение'
                                     )

    product_2 = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='В какому продукту он принадлежит',
        related_name='product_2'
    )

    name_3 = models.CharField(max_length=50, blank=True,
                              null=True, verbose_name='Имя')
    title_3 = models.CharField(max_length=50, blank=True,
                               null=True,  verbose_name='Описание')
    big_image_3 = models.ImageField(
        upload_to='banner/',
        max_length=None,
        blank=True,
        null=True,
        verbose_name='Фото сзади'
    )
    main_image_3 = models.ImageField(upload_to='banner/',
                                     blank=True,
                                     null=True,
                                     verbose_name='Основное изображение'
                                     )

    product_3 = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='В какому продукту он принадлежит',
        related_name='product_3'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = "Баннеры"


class Benefits(models.Model):
    image = models.FileField(upload_to='benefits/', blank=True,
                             null=True, verbose_name="Изображение достижений")
    title = models.CharField(max_length=50,  verbose_name="Имя достижения")
    desc = models.CharField(max_length=255, blank=True,
                            null=True,  verbose_name="Заявление о достижениях")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Успех'
        verbose_name_plural = "Преимущества"


class MainPageBanners(models.Model):
    image = models.ImageField(upload_to='main_page_banners/',
                              blank=True, null=True, verbose_name='Фото')
    image_2 = models.ImageField(upload_to='main_page_banners/',
                                blank=True, null=True, verbose_name='Фото_2')
    image_3 = models.ImageField(upload_to='main_page_banners/',
                                blank=True, null=True, verbose_name='Фото_3')
    image_4 = models.ImageField(upload_to='main_page_banners/',
                                blank=True, null=True, verbose_name='Фото_4')
    image_5 = models.ImageField(upload_to='main_page_banners/',
                                blank=True, null=True, verbose_name='Фото_5')


class TopThree(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='В какому продукту он принадлежит',)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Популярный товар'
        verbose_name_plural = "Самые популярные товары"


class News(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новинка'
        verbose_name_plural = "Новости"


class AboutBanner(models.Model):
    image = models.ImageField(upload_to='about_banners/',
                              blank=True, null=True, verbose_name='О нас фото')
    title = models.CharField(max_length=250, blank=True,
                             null=True, verbose_name='Первая линия')
    title_2 = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Вторая линия")
    title_3 = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Третья строка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = "О нас"


class AboutPageBanners(models.Model):
    image = models.ImageField(upload_to='main_page_banners/',
                              blank=True, null=True, verbose_name='О нас')
    image_2 = models.ImageField(upload_to='main_page_banners/',
                                blank=True, null=True, verbose_name='О нас_2')
    image_3 = models.ImageField(upload_to='main_page_banners/',
                                blank=True, null=True, verbose_name='О нас_3')

    class Meta:
        verbose_name = 'Баннер о нас'
        verbose_name_plural = "Баннер о нас"


class AboutUs(models.Model):
    logo = models.ImageField(upload_to='logo', blank=True, null=True)
    title = models.CharField(max_length=250, blank=True,
                             null=True, verbose_name='Первая строка')
    title_2 = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Вторая линия")
    title_3 = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Третья строка")
    title_4 = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Четвертая строка")
    title_5 = models.TextField(
        blank=True, null=True, verbose_name="Пятая линия")

    class Meta:
        verbose_name = 'Информация о нас'
        verbose_name_plural = "Информация о нас"


class ContactUs(models.Model):

    email = models.EmailField(max_length=50, verbose_name="Email")
    name = models.CharField(max_length=100, verbose_name="Name")
    phone = models.CharField(max_length=50, verbose_name="Phone")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-created_at",)

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Форма обратной связи'


class Locations(models.Model):
    image = models.ImageField(upload_to='contact_banner/', blank=True, null=True, verbose_name='Контактный баннер')
    location = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Ваш адрес")
    open_to_work_time = models.CharField(
        max_length=255,  blank=True, null=True, verbose_name="Когда вы начнете работать")
    close_to_work_time = models.CharField(
        max_length=255,  blank=True, null=True, verbose_name="Когда вы закончите работу")
    phone_number = models.CharField(
        max_length=25, verbose_name="Ваш номер телефона")
    email = models.EmailField(max_length=50, verbose_name="Ваш адрес электронной почты")
    map = models.TextField(blank=True, null=True, verbose_name='Ваше местоположение на карте')

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'Справочная информация'
        verbose_name_plural = 'Справочная информация'


class ProductsBanner(models.Model):
    image = models.ImageField(upload_to='products_banner/',
                              blank=True, null=True, verbose_name="Баннер на товары")
    title = models.CharField(max_length=100, blank=True,
                             null=True, verbose_name="Заявление маленькое")
    title_2 = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Заявление отличное")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер на товары'
        verbose_name_plural = 'Баннер на товары'


class Flag(models.Model):
    ru = models.ImageField(upload_to="ru_flag/", blank=True, null=True)
    eng = models.ImageField(upload_to="ru_flag/", blank=True, null=True)
    tm = models.ImageField(upload_to="ru_flag/", blank=True, null=True)