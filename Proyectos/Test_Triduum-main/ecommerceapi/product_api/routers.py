from rest_framework.routers import DefaultRouter
from views import ProductViewSet, OrderViewSet, OrderDetailViewSet

# Creamos un enrutador para nuestras vistas
router = DefaultRouter()

# Registramos las vistas con el enrutador
router.register(r'products', ProductViewSet, basename='products')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'orderdetails', OrderDetailViewSet, basename='orderdetails')
