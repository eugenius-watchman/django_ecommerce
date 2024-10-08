from django.urls import path
from django.urls.conf import include
# from rest_framework.routers import DefaultRouter
# from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework_nested import routers
from . import views


# Main router
router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet, basename='collections')
router.register('carts', views.CartViewSet, basename='carts')
router.register('customers', views.CustomerViewSet, basename='customers')
router.register('orders', views.OrderViewSet, basename='orders')

# Nested router for products
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')



#URL Conf
urlpatterns = router.urls + products_router.urls + carts_router.urls


# urlpatterns = [
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:pk>', views.ProductDetail.as_view()),
#     path('collections/', views.CollectionList.as_view()),
#     path('collections/<int:pk>', views.CollectionDetail.as_view(), name='collection-detail')
# ]