# expenses/views.py
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Expense
from .serializers import ExpenseSerializer
from .utils import download_balance_sheet_csv

class ExpenseCreateView(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def perform_create(self, serializer):
        expense = serializer.save()
        if expense.split_method == 'percentage' and sum(expense.amounts.values()) != 100:
            raise ValidationError("Percentages must add up to 100%")

class ExpenseListView(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class BalanceSheetView(APIView):
    def get(self, request):
        balance_sheet = {}
        for expense in Expense.objects.all():
            splits = expense.calculate_splits()
            for user_id, amount in splits.items():
                if user_id not in balance_sheet:
                    balance_sheet[user_id] = 0
                balance_sheet[user_id] += amount
        return Response(balance_sheet)

class DownloadBalanceSheetView(APIView):
    def get(self, request):
        balance_sheet = {}  # Same calculation logic as BalanceSheetView
        for expense in Expense.objects.all():
            splits = expense.calculate_splits()
            for user_id, amount in splits.items():
                if user_id not in balance_sheet:
                    balance_sheet[user_id] = 0
                balance_sheet[user_id] += amount
        return download_balance_sheet_csv(balance_sheet)
