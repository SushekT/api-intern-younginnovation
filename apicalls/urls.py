
from django.urls import path, include
from apicalls import views
urlpatterns = [
    path('', views.test),
    path('product_sales_by_country', views.product_sales_by_country, name="product_sales_by_country"),
    path('two_years/', views.two_years, name='two_years'),
    path('leastsale/', views.leastsale, name='leastsale'),
]
