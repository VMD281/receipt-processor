from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Receipt
import uuid


from django.http import JsonResponse

def api_index(request):
    return JsonResponse({
        "message": "Welcome to the Receipt Processor API. Available endpoints:",
        "endpoints": {
            "Process Receipts": "/api/receipts/process (POST)",
            "Get Points": "/api/receipts/<id>/points (GET)"
        }
    })

def calculate_points(receipt):
    points = 0
    # Points based on retailer name
    points += sum(1 for c in receipt['retailer'] if c.isalnum())
    # Points if total is a round number
    if float(receipt['total']).is_integer():
        points += 50
    # Points if total is multiple of 0.25
    if float(receipt['total']) % 0.25 == 0:
        points += 25
    # Points based on item count
    points += (len(receipt['items']) // 2) * 5
    # Points based on purchase day
    if int(receipt['purchase_date'].split('-')[2]) % 2 == 1:
        points += 6
    # Points based on purchase time
    time = int(receipt['purchase_time'].split(':')[0])
    if 14 <= time < 16:
        points += 10
    return points

class ProcessReceiptView(APIView):
    def post(self, request):
        receipt_data = request.data
        points = calculate_points(receipt_data)
        receipt = Receipt.objects.create(
            retailer=receipt_data['retailer'],
            purchase_date=receipt_data['purchase_date'],
            purchase_time=receipt_data['purchase_time'],
            total=receipt_data['total'],
            points=points,
        )
        return Response({'id': receipt.id}, status=status.HTTP_201_CREATED)

class GetPointsView(APIView):
    def get(self, request, receipt_id):
        try:
            receipt = Receipt.objects.get(id=receipt_id)
            return Response({'points': receipt.points}, status=status.HTTP_200_OK)
        except Receipt.DoesNotExist:
            return Response({'error': 'Receipt not found'}, status=status.HTTP_404_NOT_FOUND)


