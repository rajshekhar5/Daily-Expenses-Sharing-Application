
# expenses/urls.py
from django.urls import path
from .views import ExpenseCreateView, ExpenseListView, BalanceSheetView, DownloadBalanceSheetView

urlpatterns = [
    path('', ExpenseCreateView.as_view(), name='expense-create'),
    path('list/', ExpenseListView.as_view(), name='expense-list'),
    path('balance-sheet/', BalanceSheetView.as_view(), name='balance-sheet'),
    path('download/', DownloadBalanceSheetView.as_view(), name='download-balance-sheet'),
]
