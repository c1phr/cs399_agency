from django.db import models

# Model to store data about the form
class form(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 254)
    phone_number = models.IntegerField()
    created = models.DateTimeField(auto_now_add = True)

	