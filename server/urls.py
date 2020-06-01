"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from .view import home
from cores.views import (
    ConfigListAPIView,
    ConfigCreateAPIView,
    ConfigRetrieveAPIView,
    ConfigUpdateAPIView,
    ConfigDestroyAPIView
)
from stocks.views.Stock import (
    StockAPIView,
    StockFilterAPIView,
    StockViewSet,
    StockScanAPIView,
    DecisiveIndexViewSet
)
from stocks.views.company import (
    CompanyViewSet,
    CompanyUpdateAPIView,
    CompanyInfoFilterAPIView,
    SubCompanyAPIView,
    SubCompanyUpdateAPIView,
    CompanyOfficerAPIView,
    CompanyOfficerUpdateAPIView,
    CompanyTransactionsAPIView,
    CompanyTransactionsUpdateAPIView,
    CompanyHistoricalQuoteRetrieveAPIView,
    CompanyHistoricalQuoteUpdateAPIView
)
from stocks.views.HistoricalQuote import HistoricalQuoteAPIView
from stocks.views.Finance import (
    LatestFinancialInfoRetrieveAPIView,
    LatestFinancialInfoUpdateAPIView,
    LatestFinancialInfoFilterAPIView,
    YearlyFinancialInfoRetrieveAPIView,
    YearlyFinancialInfoUpdateAPIView,
    YearlyFinancialInfoFilterAPIView,
    QuarterlyFinancialInfoRetrieveAPIView,
    QuarterlyFinancialInfoUpdateAPIView,
    QuarterlyFinancialInfoFilterAPIView,
    LastestFinancialReportsRetrieveAPIView,
    LastestFinancialReportsNameUpdateAPIView,
    LastestFinancialReportsValueUpdateAPIView,
)
from stocks.views.IntradayQuote import IntradayQuoteAPIView
from stocks.views.Analysis import AnalysisListAPIView, StockNewsAPIView
from stocks.views.MarketNews import (
    AllNewsApiView,
    PositiveNewsApiView,
    NegativeNewsApiView,
    NewsInGroupApiView
)

from notes.views import NoteViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'api/Note', NoteViewSet, basename='note')
router.register(r'api2/Stock', StockViewSet, basename='stock')
router.register(r'api/Company', CompanyViewSet, basename='company')
router.register(r'api/DecisiveIndex', DecisiveIndexViewSet, basename='decisiveIndex')

urlpatterns = router.urls

urlpatterns = router.urls + [
    path('django-rq/', include('django_rq.urls')),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/config/', ConfigListAPIView.as_view()),
    # path('api/config/', ConfigCreateAPIView.as_view()),
    # path('api/config/', ConfigRetrieveAPIView.as_view()),
    path('api/config/<int:pk>/', ConfigUpdateAPIView.as_view()),
    # path('api/config/<int:pk>/', ConfigDestroyAPIView.as_view()),
    # 
    path('api/Data/Markets/TradingStatistic/', StockAPIView.as_view()),
    # 
    # path('api/Data/Companies/CompanyInfo/', CompanyListAPIView.as_view()),
    path('api/Data/Companies/CompanyInfo/update/', CompanyUpdateAPIView.as_view()),
    path('api/Data/Companies/CompanyInfo/filter/', CompanyInfoFilterAPIView.as_view()),
    path('api/Data/Companies/SubCompanies/', SubCompanyAPIView.as_view()),
    path('api/Data/Companies/SubCompanies/update/', SubCompanyUpdateAPIView.as_view()),
    path('api/Data/Companies/CompanyOfficers/', CompanyOfficerAPIView.as_view()),
    path('api/Data/Companies/CompanyOfficers/update/', CompanyOfficerUpdateAPIView.as_view()),
    path('api/Data/Companies/CompanyTransactions/', CompanyTransactionsAPIView.as_view()),
    path('api/Data/Companies/CompanyTransactions/update/', CompanyTransactionsUpdateAPIView.as_view()),
    path('api/Data/Companies/HistoricalQuotes/', CompanyHistoricalQuoteRetrieveAPIView.as_view()),
    path('api/Data/Companies/HistoricalQuotes/update/', CompanyHistoricalQuoteUpdateAPIView.as_view()),
    # 
    path('api/Data/Finance/LastestFinancialInfo/', LatestFinancialInfoRetrieveAPIView.as_view()),
    path('api/Data/Finance/LastestFinancialInfo/update/', LatestFinancialInfoUpdateAPIView.as_view()),
    path('api/Data/Finance/LastestFinancialInfo/filter/', LatestFinancialInfoFilterAPIView.as_view()),
    path('api/Data/Finance/YearlyFinancialInfo/', YearlyFinancialInfoRetrieveAPIView.as_view()),
    path('api/Data/Finance/YearlyFinancialInfo/update/', YearlyFinancialInfoUpdateAPIView.as_view()),
    path('api/Data/Finance/YearlyFinancialInfo/filter/', YearlyFinancialInfoFilterAPIView.as_view()),
    path('api/Data/Finance/QuarterlyFinancialInfo/', QuarterlyFinancialInfoRetrieveAPIView.as_view()),
    path('api/Data/Finance/QuarterlyFinancialInfo/update/', QuarterlyFinancialInfoUpdateAPIView.as_view()),
    path('api/Data/Finance/QuarterlyFinancialInfo/filter/', QuarterlyFinancialInfoFilterAPIView.as_view()),
    path('api/Data/Finance/LastestFinancialReports/', LastestFinancialReportsRetrieveAPIView.as_view()),
    path('api/Data/Finance/LastestFinancialReportsName/update/', LastestFinancialReportsNameUpdateAPIView.as_view()),
    path('api/Data/Finance/LastestFinancialReportsValue/update/', LastestFinancialReportsValueUpdateAPIView.as_view()),
    # 

    path('api/Analysis/', AnalysisListAPIView.as_view()),
    path('api/Stock/Filter/', StockFilterAPIView.as_view()),
    path('api/Stock/scan/', StockScanAPIView.as_view()),
    path('api/Stock/News/', StockNewsAPIView.as_view()),
    #
    path('api/Data/News/AllNews', AllNewsApiView.as_view()),
    path('api/Data/News/PositiveNews', PositiveNewsApiView.as_view()),
    path('api/Data/News/NegativeNews', NegativeNewsApiView.as_view()),
    path('api/Data/News/NewsInGroup', NewsInGroupApiView.as_view()),
    # 

    # path('api/Data/Companies/HistoricalQuotes/', HistoricalQuoteAPIView.as_view()),
    # path('api/Data/Companies/CompanyInfo/', IntradayQuoteAPIView.as_view()),
    # url(r'^api-auth/', include('rest_framework.urls'))
]



