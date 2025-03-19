
from django.urls import path
from .views import get_loans, create_loan, loan_detail

urlpatterns = [
    path('loans/', get_loans, name='get_loans'),
    path('loans/create/', create_loan, name='create_loan'),
    path('loans/<int:pk>', loan_detail, name='loan_detail')
]