from django.db import models

# Create your models here.
class Character(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Name')
    status = models.CharField(max_length=200, verbose_name='Status')
    species = models.CharField(max_length=200, verbose_name='Species')
    gender = models.CharField(max_length=200, verbose_name='Gender')
    image = models.URLField(max_length=200, verbose_name='URL Image')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
