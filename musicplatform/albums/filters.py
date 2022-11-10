from .models import Album
from django_filters import rest_framework

class FilteringAlbum (rest_framework.FilterSet):
    name = rest_framework.CharFilter(lookup_expr='icontains')
    cost_greaterthanOrEqual = rest_framework.NumberFilter(field_name="cost", lookup_expr='gte')
    cost_LessthanOrEqual = rest_framework.NumberFilter(field_name="cost", lookup_expr='lte')
    
    class Meta:
        model = Album
        fields = ['cost', 'name']

