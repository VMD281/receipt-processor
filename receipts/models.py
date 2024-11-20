from django.db import models

# Create your models here.

class Receipt(models.Model):
    retailer = models.CharField(max_length=255)
    purchase_date = models.DateField()
    purchase_time = models.TimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.retailer} - {self.purchase_date}"
