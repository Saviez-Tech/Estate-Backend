# filters.py
import django_filters
from .models import Property

class PropertyFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    bedrooms = django_filters.NumberFilter(field_name="bedrooms", lookup_expr='exact')
    bathrooms = django_filters.NumberFilter(field_name="bathrooms", lookup_expr='exact')
    location = django_filters.CharFilter(field_name="location_city", lookup_expr='icontains')
    property_type = django_filters.CharFilter(field_name="property_type", lookup_expr='icontains')
    # Add other filters as needed, e.g., area, designation, batch, roles etc.

    class Meta:
        model = Property
        fields = ['location', 'property_type', 'price_min', 'price_max', 'bedrooms', 'bathrooms']
