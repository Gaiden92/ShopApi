from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shop.views import CategoryViewSet, ProductViewSet, ArticleViewSet

# création du routeur
router = routers.SimpleRouter()

# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
