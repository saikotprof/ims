from django.urls import path
from .import views
from .views import index, product, apple, samsung, xiaomi


urlpatterns = [
    path('', index, name='home'),
    path('products/', product, name='product-details'),
    path('apple/', apple, name='apple'),
    path('samsung/', samsung, name='samsung'),
    path('xiaomi/', xiaomi, name='xiaomi'),
    path('apple/new/', views.AppleCreateView.as_view(), name='apple-new'),
    path('samsung/new/', views.SamsungCreateView.as_view(), name='samsung-new'),
    path('xiaomi/new/', views.XiaomiCreateView.as_view(), name='xiaomi-new'),
    path('apple/<int:pk>/edit/', views.AppleUpdateView.as_view(), name='apple-update'),
    path('samsung/<int:pk>/edit/', views.SamsungUpdateView.as_view(), name='samsung-update'),
    path('xiaomi/<int:pk>/edit/', views.XiaomiUpdateView.as_view(), name='xiaomi-update'),
    path('apple/<int:pk>/delete/', views.AppleDeleteView.as_view(), name='apple-delete'),
    path('samsung/<int:pk>/delete/', views.SamsungDeleteView.as_view(), name='samsung-delete'),
    path('xiaomi/<int:pk>/delete/', views.XiaomiDeleteView.as_view(), name='xiaomi-delete'),
]