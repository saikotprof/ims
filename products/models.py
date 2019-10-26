from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class Device(models.Model):
    name = models.CharField(max_length=40)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()

    choose = [
        ('Sold', 'Item already purchased'),
        ('Sold Out', 'Item comming soon'),
        ('Available', 'Item ready to purchase'),
    ]

    status = models.CharField(max_length=30, choices=choose, default='Sold')
    remarks = models.CharField(max_length=50, default='No Issues')


    def __str__(self):
        return f"{self.name} - {self.brand} - {self.price}"


class Apple(Device):
    pass


class Samsung(Device):
    pass


class Xiaomi(Device):
    pass
