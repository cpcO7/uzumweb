from django_filters import FilterSet, CharFilter


class DistrictFilter(FilterSet):
    title = CharFilter(field_name='country', lookup_expr='icontains')
