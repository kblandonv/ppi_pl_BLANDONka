from rest_framework.routers import DefaultRouter
from views import ProductViewSet, OrderViewSet, OrderDetailViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'orderdetails', OrderDetailViewSet, basename='orderdetails')
router.register(r'create', OrderDetailViewSet, basename='create')
