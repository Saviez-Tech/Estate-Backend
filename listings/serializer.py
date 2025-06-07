from rest_framework import serializers
from .models import Property,PropertyImage,BankPaymentInfo, CryptoPaymentInfo,ContactMessage,NewsletterSubscriber

class BankPaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankPaymentInfo
        fields = ['bank_name', 'account_number', 'account_name']

class CryptoPaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoPaymentInfo
        fields = ['name', 'wallet_address', 'instructions']


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image', 'alt_text']


class HouseSerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    class Meta:
        model = Property
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'


class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']