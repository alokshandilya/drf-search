from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=7, default=149.99)

    @property
    def sale_price(self):
        sale_price = float(self.price) * 0.8  # 20% off
        return f"{sale_price:.2f}"

    def get_owner_msg(self):
        msg = f"Alok Shandilya is {self.title}'s owner"
        return msg

    def __str__(self):
        return f"{self.title} | Rs. {self.price}"
