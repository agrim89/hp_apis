from rest_framework import serializers
from .models import PartnerSalesTeam, Partner

Gender = ("male", "female")


class BaseUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=50)
    dealer_name = serializers.CharField(max_length=100)
    mobile = serializers.CharField(max_length=10)
    address = serializers.CharField(max_length=1000)
    gender = serializers.ChoiceField(choices=Gender)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return PartnerSalesTeam.objects.create(**validated_data)


class CompanySerializer(serializers.Serializer):
    company_name = serializers.CharField(max_length=1000)
    domain_name = serializers.CharField(max_length=1000)
    partner_id = serializers.CharField(max_length=100)
    region = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=100)
    dedicated_person = serializers.CharField(max_length=100)
    email_id = serializers.EmailField()
    mobile = serializers.CharField(max_length=10)
    status = serializers.BooleanField(default=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Partner.objects.create(**validated_data)
