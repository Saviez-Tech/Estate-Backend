from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Property,BankPaymentInfo,CryptoPaymentInfo, PaymentReceipt
from .serializer import HouseSerializer,BankPaymentInfoSerializer,CryptoPaymentInfoSerializer,ContactMessageSerializer,NewsletterSubscriberSerializer
from rest_framework.views import APIView
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination

# List view: List all houses
@api_view(['GET'])
@permission_classes([])
def property_list(request):
    houses = Property.objects.all()
    
    paginator = PageNumberPagination()
    paginator.page_size = 1  # or whatever number you want per page
    
    result_page = paginator.paginate_queryset(houses, request)
    serializer = HouseSerializer(result_page, many=True)
    
    return paginator.get_paginated_response(serializer.data)

# Detail view: Retrieve one house by ID
@api_view(['GET'])
@permission_classes([])
def property_detail(request, pk):
    try:
        property = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return Response({'error': 'Property not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = HouseSerializer(property)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def bank_payment_info(request):
    try:
        bank_info = BankPaymentInfo.objects.first()
        if not bank_info:
            return Response({'detail': 'Bank payment info not set'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BankPaymentInfoSerializer(bank_info)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def crypto_payment_info_list(request):
    cryptos = CryptoPaymentInfo.objects.all()
    serializer = CryptoPaymentInfoSerializer(cryptos, many=True)
    return Response(serializer.data)


class PaymentReceiptCreateView(APIView):
    permission_classes = [permissions.AllowAny]  # Adjust permissions as needed

    def post(self, request):
        # Required fields
        property_id = request.data.get('property')
        full_name = request.data.get('full_name')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        message = request.data.get('message', '')
        receipt_image = request.FILES.get('receipt_image')

        if not all([property_id, full_name, email, phone_number, receipt_image]):
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

        property_obj = get_object_or_404(Property, id=property_id)

        payment_receipt = PaymentReceipt.objects.create(
            property=property_obj,
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            message=message,
            receipt_image=receipt_image,
        )

        return Response({
            'message': 'Payment receipt uploaded successfully',
            'id': payment_receipt.id
        }, status=status.HTTP_201_CREATED)
    

@api_view(['POST'])
@permission_classes([])
def contact_message_create(request):
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Your message has been sent successfully.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([])
def subscribe_newsletter(request):
    serializer = NewsletterSubscriberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Successfully subscribed to newsletter.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)