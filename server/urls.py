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
from stocks.views.Company import CompanyAPIView, SubCompanyAPIView
from stocks.views.HistoricalQuote import HistoricalQuoteAPIView
from stocks.views.LatestFinancialInfo import LatestFinancialInfoAPIView
from stocks.views.IntradayQuote import IntradayQuoteAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/Data/Companies/CompanyInfo/', CompanyAPIView.as_view()),
    path('api/Data/Companies/HistoricalQuotes/', HistoricalQuoteAPIView.as_view()),
    path('api/Data/Finance/LastestFinancialInfo/', LatestFinancialInfoAPIView.as_view()),
    path('api/Data/Companies/CompanyInfo/', IntradayQuoteAPIView.as_view()),
    path('api/Data/Companies/SubCompanies/', SubCompanyAPIView.as_view()),
    # url(r'^api-auth/', include('rest_framework.urls'))
]
