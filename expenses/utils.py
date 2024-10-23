# expenses/utils.py
import csv
from django.http import HttpResponse

def download_balance_sheet_csv(balance_sheet):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="balance_sheet.csv"'
    writer = csv.writer(response)
    writer.writerow(['User ID', 'Amount Owed'])
    for user_id, amount in balance_sheet.items():
        writer.writerow([user_id, amount])
    return response
