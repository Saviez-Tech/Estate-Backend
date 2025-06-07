from django.contrib import admin
from .models import Property, PropertyImage,CryptoPaymentInfo,BankPaymentInfo,ContactMessage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3  # Number of extra blank images to show

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'price', 'location_city', 'location_state')
    inlines = [PropertyImageInline]


admin.site.register(CryptoPaymentInfo)
admin.site.register(BankPaymentInfo)
admin.site.register(ContactMessage)