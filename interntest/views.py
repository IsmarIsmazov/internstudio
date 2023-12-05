from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from .models import Bank
from .serializers import BankSerializer


# Create your views here.
def create1():
    Bank.objects.create()


def create2():
    Bank.objects.create()


@api_view(['GET'])
def createall(request):
    create1()
    create2()
    return JsonResponse(
        data={
            'status': '2000',
            'errors': 'Null'
        }
    )
