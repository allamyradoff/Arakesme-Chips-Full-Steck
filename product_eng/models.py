from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True,
                            null=True, verbose_name='Ady')
    icon = models.FileField(upload_to='icon/', blank=True,
                            null=True, verbose_name='Ikonkasy')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriýa'
        verbose_name_plural = "Kategoriýalar"


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ady')
    image = models.ImageField(upload_to='product/',
                              blank=True, null=True, verbose_name='Suraty')
    image_2 = models.ImageField(upload_to='product/',
                                blank=True, null=True, verbose_name='Suraty_2')
    image_3 = models.ImageField(upload_to='product/',
                                blank=True, null=True, verbose_name='Suraty_3')
    desc = models.TextField(blank=True, null=True, verbose_name='Beýany')

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 blank=True, null=True, verbose_name='Haýsy kategoriýa degişli')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Haryt'
        verbose_name_plural = "harytlar"


class Banner(models.Model):
    name = models.CharField(max_length=50, blank=True,
                            null=True, verbose_name='Ady')
    title = models.CharField(max_length=50, blank=True,
                             null=True,  verbose_name='Beýany')
    big_image = models.ImageField(
        upload_to='banner/',
        max_length=None,
        blank=True,
        null=True,
        verbose_name='Arkadaky surat'
    )
    main_image = models.ImageField(upload_to='banner/',
                                   blank=True,
                                   null=True,
                                   verbose_name='Esasy surat'
                                   )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Haýsy haryda degişli'
    )

    name_2 = models.CharField(max_length=50, blank=True,
                              null=True, verbose_name='Ady')
    title_2 = models.CharField(max_length=50, blank=True,
                               null=True,  verbose_name='Beýany')
    big_image_2 = models.ImageField(
        upload_to='banner/', max_length=None,
        blank=True,
        null=True,
        verbose_name='Arkadaky surat'
    )
    main_image_2 = models.ImageField(upload_to='banner/',
                                     blank=True,
                                     null=True,
                                     verbose_name='Esasy surat'
                                     )

    product_2 = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Haýsy haryda degişli',
        related_name='product_2'
    )

    name_3 = models.CharField(max_length=50, blank=True,
                              null=True, verbose_name='Ady')
    title_3 = models.CharField(max_length=50, blank=True,
                               null=True,  verbose_name='Beýany')
    big_image_3 = models.ImageField(
        upload_to='banner/',
        max_length=None,
        blank=True,
        null=True,
        verbose_name='Arkadaky surat'
    )
    main_image_3 = models.ImageField(upload_to='banner/',
                                     blank=True,
                                     null=True,
                                     verbose_name='Esasy surat'
                                     )

    product_3 = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Haýsy haryda degişli',
        related_name='product_3'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = "Bannerlar"


class Benefits(models.Model):
    image = models.FileField(upload_to='benefits/', blank=True,
                             null=True, verbose_name="Üstünlikleriň suraty")
    title = models.CharField(max_length=50,  verbose_name="Üstünlikleriň ady")
    desc = models.CharField(max_length=255, blank=True,
                            null=True,  verbose_name="Üstünlikleriň beýany")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Üstünlik'
        verbose_name_plural = "Üstünlikler"


class MainPageBanners(models.Model):
    image = models.ImageField(upload_to='main_page_banners/',
                              blank=True, null=True, verbose_name='Üstunlikleriň suraty')
    image_2 = models.ImageField(upload_to='main_page_banners/',
                                blank=True, null=True, verbose_name='Üstunlikleriň suraty_2')
    image_3 = models.ImageField(upload_to='main_page_banners/',
                                blank=True, null=True, verbose_name='Üstunlikleriň suraty_3')
    image_4 = models.ImageField(upload_to='main_page_banners/',
                                blank=True, null=True, verbose_name='Üstunlikleriň suraty_4')
    image_5 = models.ImageField(upload_to='main_page_banners/',
                                blank=True, null=True, verbose_name='Üstunlikleriň suraty_5')


class TopThree(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Meşhur haryt'
        verbose_name_plural = "Iň meşhur harytlar"


class News(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Täzelik'
        verbose_name_plural = "Täzelikler"


class AboutBanner(models.Model):
    image = models.ImageField(upload_to='about_banners/',
                              blank=True, null=True, verbose_name='Biz barada suraty')
    title = models.CharField(max_length=250, blank=True,
                             null=True, verbose_name='Birinji setir')
    title_2 = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Ikinji setir")
    title_3 = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Üçinji setir")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Biz barada'
        verbose_name_plural = "Biz barada"


class AboutPageBanners(models.Model):
    image = models.ImageField(upload_to='main_page_banners/',
                              blank=True, null=True, verbose_name='Biz barada  suraty')
    image_2 = models.ImageField(upload_to='main_page_banners/',
                                blank=True, null=True, verbose_name='Biz barada  suraty_2')
    image_3 = models.ImageField(upload_to='main_page_banners/',
                                blank=True, null=True, verbose_name='Biz barada  suraty_3')

    class Meta:
        verbose_name = 'Biz barada banner'
        verbose_name_plural = "Biz barada banner"


class AboutUs(models.Model):
    logo = models.ImageField(upload_to='logo', blank=True, null=True)
    title = models.CharField(max_length=250, blank=True,
                             null=True, verbose_name='Birinji setir')
    title_2 = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Ikinji setir")
    title_3 = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Üçinji setir")
    title_4 = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Dördinji setir")
    title_5 = models.TextField(
        blank=True, null=True, verbose_name="Bäşinji setir")

    class Meta:
        verbose_name = 'Biz barada maglumat'
        verbose_name_plural = "Biz barada maglumatlar"


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
        verbose_name = 'Aragatnaşyk formasy'
        verbose_name_plural = 'Aragatnaşyk formasy'


class Locations(models.Model):
    image = models.ImageField(upload_to='contact_banner/', blank=True, null=True, verbose_name='Konataktdaky banner')
    location = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Salgyňyz")
    open_to_work_time = models.CharField(
        max_length=255,  blank=True, null=True, verbose_name="Işe başlaýan wagtyňyz")
    close_to_work_time = models.CharField(
        max_length=255,  blank=True, null=True, verbose_name="Işi gutarýan wagtyňyz")
    phone_number = models.CharField(
        max_length=25, verbose_name="Telefon belgiňiz")
    email = models.EmailField(max_length=50, verbose_name="E-poçtaňyz")
    map = models.TextField(blank=True, null=True, verbose_name='Kartada ýerleşýän ýeriňiz')

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'Salgylar barada maglumat'
        verbose_name_plural = 'Salgylar barada maglumatlar'


class ProductsBanner(models.Model):
    image = models.ImageField(upload_to='products_banner/',
                              blank=True, null=True, verbose_name="Harytlardaky banner")
    title = models.CharField(max_length=100, blank=True,
                             null=True, verbose_name="Beýan kiçi")
    title_2 = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Beýan uly")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Harytlardaky banner'
        verbose_name_plural = 'Harytlardaky bannerlar'


class Flag(models.Model):
    ru = models.ImageField(upload_to="ru_flag/", blank=True, null=True)
    eng = models.ImageField(upload_to="ru_flag/", blank=True, null=True)
    tm = models.ImageField(upload_to="ru_flag/", blank=True, null=True)