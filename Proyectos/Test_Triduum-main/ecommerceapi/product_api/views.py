from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from product_api.models import Product, Order, OrderDetail
from product_api.serializers import ProductSerializer, OrderSerializer, OrderDetailSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar productos.

    Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los productos.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        """
        Crea un nuevo producto.

        Args:
            request: Request con los datos del producto a crear.

        Returns:
            Response con los datos del producto creado y código de estado HTTP 201 (Created).
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        """
        Obtiene la lista de todos los productos.

        Returns:
            Response con la lista de productos y código de estado HTTP 200 (OK).
        """
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Elimina un producto.

        Si el producto tiene stock mayor a cero, devuelve un error HTTP 400 (Bad Request).

        Args:
            request: Request con los datos del producto a eliminar.

        Returns:
            Response con código de estado HTTP 204 (No Content) si se eliminó correctamente o
            código de estado HTTP 400 (Bad Request) si no se pudo eliminar.
        """
        instance = self.get_object()
        if instance.stock > 0:
            return Response({'error': 'Cannot delete a product with stock'}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        """
        Actualiza un producto existente.

        Args:
            request: Request con los datos actualizados del producto.

        Returns:
            Response con los datos actualizados del producto y código de estado HTTP 200 (OK).
        """
        instance = self.get_object()
        serializer = ProductSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """
        Actualiza parcialmente un producto existente.

        Args:
            request: Request con los datos parcialmente actualizados del producto.

        Returns:
            Response con los datos actualizados del producto y código de estado HTTP 200 (OK).
        """
        instance = self.get_object()
        serializer = ProductSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar órdenes.

    Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre las órdenes.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        """
        Crea una nueva orden.

        Args:
            request: Request con los datos de la orden a crear.

        Returns:
            Response con los datos de la orden creada y código de estado HTTP 201 (Created).
        """
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        """
        Elimina una orden.

        Args:
            request: Request con los datos de la orden a eliminar.

        Returns:
            Response con código de estado HTTP 204 (No Content) si se eliminó correctamente.
        """
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        """
        Actualiza una orden existente.

        Args:
            request: Request con los datos actualizados de la orden.

        Returns:
            Response con los datos actualizados de la orden y código de estado HTTP 200 (OK).
        """
        instance = self.get_object()
        serializer = OrderSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """
        Actualiza parcialmente una orden existente.

        Args:
            request: Request con los datos parcialmente actualizados de la orden.

        Returns:
            Response con los datos actualizados de la orden y código de estado HTTP 200 (OK).
        """
        instance = self.get_object()
        serializer = OrderSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class OrderDetailViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar detalles de órdenes.

    Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los detalles de las órdenes.
    """
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

    def create(self, request, *args, **kwargs):
        """
        Crea un nuevo detalle de orden.

        Args:
            request: Request con los datos del detalle de orden a crear.

        Returns:
            Response con los datos del detalle de orden creado y código de estado HTTP 201 (Created).
        """
        serializer = OrderDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        """
        Elimina un detalle de orden.

        Args:
            request: Request con los datos del detalle de orden a eliminar.

        Returns:
            Response con código de estado HTTP 204 (No Content) si se eliminó correctamente.
        """
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        """
        Actualiza un detalle de orden existente.

        Args:
            request: Request con los datos actualizados del detalle de orden.

        Returns:
            Response con los datos actualizados del detalle de orden y código de estado HTTP 200 (OK).
        """
        instance = self.get_object()
        serializer = OrderDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """
        Actualiza parcialmente un detalle de orden existente.

        Args:
            request: Request con los datos parcialmente actualizados del detalle de orden.

        Returns:
            Response con los datos actualizados del detalle de orden y código de estado HTTP 200 (OK).
        """
        instance = self.get_object()
        serializer = OrderDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
