# expenses/serializers.py
from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'description', 'amount', 'date', 'paid_by', 'participants', 'split_method', 'amounts')
