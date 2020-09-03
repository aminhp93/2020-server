# import django_filters
# from stocks.models import Stock
# from django.db.models import Q, F


# class StockFilterIsVN30Queryset(django_filters.Filter):
#     def filter(self, qs, value):
#         if not value:
#             return qs
#         if value:
#             return qs.filter(IsVN30=True)
#         return qs.none()


# class StockFilter(django_filters.FilterSet):
#     IsVN30 = StockFilterIsVN30Queryset()

#     class Meta:
#         model = Stock
#         fields = ('IsVN30')