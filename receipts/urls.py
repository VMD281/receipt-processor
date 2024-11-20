from django.urls import path
from . import views  # Ensure this correctly points to views in the `receipts` app

urlpatterns = [
    path('', views.api_index, name='api-index'),
    path('receipts/process', views.ProcessReceiptView.as_view(), name='process-receipt'),
    path('receipts/<str:receipt_id>/points', views.GetPointsView.as_view(), name='get-points'),
]
