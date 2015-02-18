from django.db import models

# Model to store data about the form
class form(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 254)
    phone_number = models.IntegerField()
    created = models.DateTimeField(auto_now_add = True)

class share_form(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sender_email = models.EmailField(max_length=254)
    receiver_email = models.EmailField(max_length=254)
    sender_phone = models.CharField(max_length=20)
    receiver_phone = models.CharField(max_length=20)
    sent = models.DateTimeField(auto_now_add = True)