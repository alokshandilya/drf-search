from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=7, default=149.99)

    def __str__(self):
        return f"{self.title} | Rs. {self.price}"
