from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class CustomCustomerModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer_id = models.CharField()
    name = models.CharField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_id}"
