from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=3)
    purchases = models.TextField(blank=True, null=True)
    took_on = models.DateTimeField()
    returned_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'debts_customer'

    def __str__(self):
        return f"{self.last_name} {self.first_name} ma'lumotlari"

    @property
    def is_returned(self):
        return self.returned_on is not None
