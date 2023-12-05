from rest_framework.serializers import ModelSerializer

from interntest.models import Bank


class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank
        fields = ['text']