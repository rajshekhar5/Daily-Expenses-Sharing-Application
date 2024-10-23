# expenses/models.py
from django.db import models
from users.models import User
from django.core.exceptions import ValidationError

class Expense(models.Model):
    SPLIT_METHOD_CHOICES = [
        ('equal', 'Equal'),
        ('exact', 'Exact'),
        ('percentage', 'Percentage'),
    ]

    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # This should be the current field name
    date = models.DateField(auto_now_add=True)  # Ensure this line is included for date
    paid_by = models.ForeignKey(User, related_name='expenses_paid', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='expenses_participated')
    split_method = models.CharField(max_length=20, choices=SPLIT_METHOD_CHOICES)
    amounts = models.JSONField(default=dict)  # Change to JSONField for storing split amounts

    def __str__(self):
        return f"{self.description} - {self.amount}"

    def calculate_splits(self):
        if self.split_method == 'equal':
            amount_per_person = self.amount / self.participants.count()
            return {user.id: amount_per_person for user in self.participants.all()}
        elif self.split_method == 'exact':
            return self.amounts  # Make sure amounts is structured as needed
        elif self.split_method == 'percentage':
            if sum(self.amounts.values()) != 100:
                raise ValidationError("Percentages must add up to 100%")
            return {user.id: self.amount * (percentage / 100) for user, percentage in self.amounts.items()}
