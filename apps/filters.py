from django_filters import FilterSet, CharFilter


class DistrictFilter(FilterSet):
    region = CharFilter(field_name='region_id', lookup_expr='exact')
