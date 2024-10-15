from django.urls import path
from .views import CreateProductView, CreateCategoryView

urlpatterns = [
    path('product/', CreateProductView.as_view(), name='add_product'),
    path('category/', CreateCategoryView.as_view(), name='add_category'),
]