from django.shortcuts import render
from rest_framework.views import APIView
from django.db import transaction, IntegrityError
from rest_framework import status
from interntest import serializers
from rest_framework.response import Response


class ProductAPIView(APIView):

    def post(self, request):
        try:
            with transaction.atomic():
                serializer = serializers.ProductSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

            return Response(data={"data": serializer.data}, status=status.HTTP_200_OK)

        except IntegrityError:
            return Response(
                data={"message": "ERROR",
                      "info": f"UNIQUE constraint failed: borrower with contract_number "
                              f"'{request.data['contract_number']}' already exist",
                      "payload": "Ilya cool boy!"},
                status=status.HTTP_400_BAD_REQUEST)
