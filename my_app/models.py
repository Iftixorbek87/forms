from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    exist = models.BooleanField(default=True)

    def str(self):
        return self.first_name
