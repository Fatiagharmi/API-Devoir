from django.db import models

# Create your models here.
class User (models.Model):
    username = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=100, blank=True, default='')
    pub_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.IntegerField()



class Order(models.Model):
    client = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    article = models.ForeignKey('Book', related_name='orders', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

