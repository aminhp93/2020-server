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
from django.urls import path
from .view import home
from stocks.views.Stock import StockAPIView
from stocks.views.Company import (
    CompanyListAPIView,
    CompanyUpdateAPIView,
    SubCompanyAPIView,
    SubCompanyUpdateAPIView,
    CompanyOfficerAPIView,
    CompanyOfficerUpdateAPIView,
    CompanyTransactionsAPIView,
    CompanyTransactionsUpdateAPIView
)
from stocks.views.HistoricalQuote import HistoricalQuoteAPIView
from stocks.views.Finance import (
    LatestFinancialInfoRetrieveAPIView,
    LatestFinancialInfoUpdateAPIView,
    YearlyFinancialInfoRetrieveAPIView,
    YearlyFinancialInfoUpdateAPIView
)
from stocks.views.IntradayQuote import IntradayQuoteAPIView
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # 
    path('api/Data/Markets/TradingStatistic/', StockAPIView.as_view()),
    # 
    path('api/Data/Companies/CompanyInfo/', CompanyListAPIView.as_view()),
    path('api/Data/Companies/CompanyInfo/update/', CompanyUpdateAPIView.as_view()),
    path('api/Data/Companies/SubCompanies/', SubCompanyAPIView.as_view()),
    path('api/Data/Companies/SubCompanies/update/', SubCompanyUpdateAPIView.as_view()),
    path('api/Data/Companies/CompanyOfficers/', CompanyOfficerAPIView.as_view()),
    path('api/Data/Companies/CompanyOfficers/update/', CompanyOfficerUpdateAPIView.as_view()),
    path('api/Data/Companies/CompanyTransactions/', CompanyTransactionsAPIView.as_view()),
    path('api/Data/Companies/CompanyTransactions/update/', CompanyTransactionsUpdateAPIView.as_view()),
    # 
    path('api/Data/Finance/LastestFinancialInfo/', LatestFinancialInfoRetrieveAPIView.as_view()),
    path('api/Data/Finance/LastestFinancialInfo/update/', LatestFinancialInfoUpdateAPIView.as_view()),
    path('api/Data/Finance/YearlyFinancialInfo/', YearlyFinancialInfoRetrieveAPIView.as_view()),
    path('api/Data/Finance/YearlyFinancialInfo/update/', YearlyFinancialInfoUpdateAPIView.as_view()),
    # path('test/', YearlyFinancialInfoUpdateAPIView.as_view()),
    # 
    # path('api/Data/Companies/HistoricalQuotes/', HistoricalQuoteAPIView.as_view()),
    # path('api/Data/Companies/CompanyInfo/', IntradayQuoteAPIView.as_view()),
    # url(r'^api-auth/', include('rest_framework.urls'))
]

urlpatterns += router.urls

