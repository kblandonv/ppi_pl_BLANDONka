from django.urls import path, include
from rest_framework import routers
from product_api.views import ProductViewSet, OrderViewSet, OrderDetailViewSet

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'orderdetails', OrderDetailViewSet, basename='orderdetails')
router.register(r'create', OrderDetailViewSet, basename='create')

urlpatterns = [
    path('', include(router.urls)),
]
