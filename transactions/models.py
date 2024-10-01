from django.db import models
from django.conf import settings
from customers.models import CustomCustomerModel
from django.contrib.auth.models import User


class CustomTransactionsModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomCustomerModel, on_delete=models.CASCADE, null=True)
    transaction_id = models.CharField(max_length=255, primary_key=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_id}"
