import django_filters
from .models import Products

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category',lookup_expr='iexact')
    prod_name = django_filters.CharFilter(field_name='prod_name',lookup_expr='icontains')
    prod_id = django_filters.RangeFilter(field_name='id')
    class Meta:
        model = Products
        fields = ['category','prod_name']