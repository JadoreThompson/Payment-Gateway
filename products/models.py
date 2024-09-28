from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class CustomProductsModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_id = models.CharField()
    price = models.IntegerField()
    name = models.CharField()
    description = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.invoice_id} sent from {self.user_id.email}"
