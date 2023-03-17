from django.db import models

class Bus(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name
    
class Transport(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    bus = models.ForeignKey(Bus, on_delete=models.PROTECT, related_name='transports')
    date = models.DateTimeField()
    description = models.TextField()
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='transports')

    def __str__(self):
        return f'{self.amount} {self.bus} {self.date}'
