from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class CustomInvoiceModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    invoice_id = models.CharField(primary_key=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=20)
    customer_name = models.CharField()
    customer_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.invoice_id} sent from {self.user_id.email}"
