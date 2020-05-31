from django.db import models


class Menu(models.Model):
    name = models.CharField('Name', max_length=255)
    link = models.CharField('Link', max_length=255)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self):
        return self.name


class Promo(models.Model):
    caption = models.CharField('Caption', max_length=255)
    title = models.CharField('Title', max_length=255)
    desc = models.CharField('Description', max_length=255)
    image = models.ImageField('Image', max_length=255, upload_to='images/promo')
    btn = models.CharField('Button', max_length=255)

    class Meta:
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'

    def __str__(self):
        return self.title


class Size(models.Model):
    name = models.CharField('Name', max_length=255)

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return self.name


class Trending(models.Model):
    headline = models.CharField('Headline', max_length=255)
    css_class = models.CharField('Css class', max_length=255)
    display = models.CharField('Display', max_length=255, blank=True, null=True)
    image = models.ImageField('Image', upload_to='images/trending')
    order = models.PositiveIntegerField('Order')

    class Meta:
        verbose_name = 'Trending'
        verbose_name_plural = 'Trendings'
        ordering = ['order']

    def __str__(self):
        return self.headline


class Status(models.Model):
    name = models.CharField('Name', max_length=255)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Name', max_length=255)
    img = models.ImageField('Image', upload_to='images/category')
    background = models.CharField('Background', max_length=255)
    order = models.PositiveIntegerField('Order')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['order']

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Category', blank=True, null=True, related_name='products', on_delete=models.SET_NULL)
    title = models.CharField('Name', max_length=255)
    price = models.PositiveIntegerField('Price')
    description = models.TextField('Description', blank=True, null=True)
    short_description = models.CharField('Short description', max_length=255, blank=True, null=True)
    size = models.ForeignKey(Size, blank=True, null=True, on_delete=models.SET_NULL)
    img = models.ImageField(blank=True, null=True, upload_to='images/product')
    status = models.ForeignKey(Status, verbose_name='Product status', blank=True, null=True, on_delete=models.SET_NULL)
    ratting = models.PositiveIntegerField('Ratting', blank=True, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField('Name', max_length=255)
    title = models.CharField('Title', max_length=255)
    text = models.TextField('Text')
    img = models.ImageField('Image', upload_to='images/testimonial')

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.name


class Blog(models.Model):
    img = models.ImageField('Image', upload_to='images/blog')
    title = models.CharField('Title', max_length=255)
    desc = models.TextField('Description')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField('Title', max_length=255)
    desc = models.TextField('Description')
    icon = models.CharField('Icon', max_length=255)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.title
