from django.db import models
from django.core.exceptions import ValidationError

class Property(models.Model):
    STATUS_CHOICES = [
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
        ('sold', 'Sold'),
        ('pending', 'Pending'),
    ]

    title = models.CharField(max_length=255)  # e.g. Modern Tranquility Villa
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    location_city = models.CharField(max_length=100)
    location_state = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='sale')
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    property_type = models.CharField(max_length=100)  # e.g. Detached, Bungalow
    year_built = models.PositiveIntegerField(blank=True, null=True)
    lot_size_sqft = models.PositiveIntegerField(blank=True, null=True)
    features = models.JSONField(blank=True, null=True)  # store features list e.g. ["Private pool", "Smart home"]
    main_image = models.ImageField(upload_to='properties/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    map_url = models.URLField(blank=True, null=True)  # For "View Map" link
    tour_price=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.title} - {self.location_city}"
    


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='properties/images/')
    alt_text = models.CharField(max_length=255, blank=True)  # Optional descriptive text

    def __str__(self):
        return f"Image for {self.property.title}"





class BankPaymentInfo(models.Model):
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    account_name = models.CharField(max_length=100)

    def clean(self):
        if BankPaymentInfo.objects.exists() and not self.pk:
            raise ValidationError('Only one BankPaymentInfo instance allowed.')

    def __str__(self):
        return f"Bank Payment Info - {self.bank_name}"

    class Meta:
        verbose_name = "Bank Payment Info"
        verbose_name_plural = "Bank Payment Info"


class CryptoPaymentInfo(models.Model):
    name = models.CharField(max_length=50)  # e.g., Bitcoin, Ethereum
    wallet_address = models.CharField(max_length=255)
    instructions = models.TextField(blank=True, null=True, help_text="Optional payment instructions")

    def __str__(self):
        return f"{self.name} Wallet"



class PaymentReceipt(models.Model):
    property = models.ForeignKey('Property', related_name='payment_receipts', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)
    receipt_image = models.ImageField(upload_to='payment_receipts/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Receipt from {self.full_name} for {self.property.title}"



class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name} - {self.subject}"
    
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email