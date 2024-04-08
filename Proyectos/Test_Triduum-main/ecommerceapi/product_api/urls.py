from django.urls import path, include
from rest_framework import routers
from product_api.views import ProductViewSet, OrderViewSet, OrderDetailViewSet

# Creamos un enrutador y registramos nuestros viewsets con él.
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'orderdetails', OrderDetailViewSet, basename='orderdetails')

# Definimos las URL de nuestra API
urlpatterns = [
    path('', include(router.urls)),
]
