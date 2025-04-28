from django.db import models
from django.contrib.auth.models import User

class Dish(models.Model):
    CATEGORY_CHOICES = [
        ('starter', 'Starter'),
        ('main', 'Main Course'),
        ('dessert', 'Dessert'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='dishes/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()
    special_request = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"


