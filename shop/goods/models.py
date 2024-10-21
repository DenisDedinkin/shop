from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['name']
        # db_table = 'category'  # Меняется название таблицы В БД

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='###', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=2, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        # db_table = 'product'  # Меняется название таблицы В БД

    def __str__(self):
        return self.name
