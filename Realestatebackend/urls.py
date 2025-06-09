"""
URL configuration for Realestatebackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('listings/',property_list,name='list-props'),
    path('listings/<int:pk>/',property_detail,name="property-details"),
    path('bank-details/',bank_payment_info,name="bank"),
    path('crypto/',crypto_payment_info_list,name="crypto"),
    path('payment-form/',PaymentReceiptCreateView.as_view(),name="payment-review"),
    path('contact/', contact_message_create, name='contact-message-create'),
    path('newsletter/subscribe/', subscribe_newsletter, name='subscribe-newsletter'),
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)