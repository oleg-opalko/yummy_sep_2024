from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.IntegerField()
    unit = models.CharField(max_length=10)

    photo = models.ImageField(upload_to='dishes', blank=True, null=True)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
