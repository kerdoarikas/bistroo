from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Food(models.Model):
    food_name = models.CharField(max_length=255)
    food_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField()
    full_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    half_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    is_vegetarian = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_spicy = models.BooleanField(default=False)

    def __str__(self):
        return self.food_name

class Menu(models.Model):
    menu_date = models.DateField()
    header1 = models.CharField(max_length=255, blank=True, null=True)
    header2 = models.CharField(max_length=255, blank=True, null=True)
    header3 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.menu_date}"

class MenuCategory(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.menu}"

class MenuFood(models.Model):
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.ForeignKey('Food', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.menu_category}"
