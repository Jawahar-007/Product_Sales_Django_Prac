import django_filters
from .models import Products

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category',lookup_expr='iexact')
    prod_name = django_filters.CharFilter(field_name='prod_name',lookup_expr='icontains')
#   prod_id = django_filters.RangeFilter(field_name='id')
    ppno_min = django_filters.CharFilter(method='filter_by_id_range', label='FROM PP-NO')
    ppno_max = django_filters.CharFilter(method='filter_by_id_range',label='To PP-NO')
    class Meta:
        model = Products
        fields = ['category','prod_name','ppno_min','ppno_max']

    def filter_by_id_range(self,queryset,name,value):
        if name == 'ppno_min':
            return queryset.filter(pp_no__gte=value)
        elif name == 'ppno_max':
            return queryset.filter(pp_no__lte=value)
        return queryset
    