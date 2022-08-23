from django.urls import path
from . import views

app_name = 'Ekartapp'
urlpatterns = [

    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='Products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='proCatdetail'),
]
