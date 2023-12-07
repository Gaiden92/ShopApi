from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Category, Product, Article
from shop.serializers import CategorySerializer, ProductSerializer, ArticleSerializer

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
# class CategoryApiView(APIView):
#     # on réécrit la méthode get
#     def get(self, *args, **kwargs):
#         # on récupere tous nos catégories
#         categories = Category.objects.all()
#         # on crée notre serializer
#         serializer = CategorySerializer(categories, many=True) # on précise many si notre itérable contient plusieurs élements

#         return Response(serializer.data) # appeler l'attribut data pour récuperer les données sérialisés
    
# création d'un model de vue pour les opération crud via Modelviewset. 
# permettre uniquement la lecture dans notre cas donc nous allons utiliser ReadOnlyModevlViewSet
class CategoryViewSet(ReadOnlyModelViewSet):
    # toujours réécrire le serializer_class et le get_queryset
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(active=True)


# class ProductApiView(APIView):

#     def get(self, *args, **kwargs):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)

#         return Response(serializer.data)

class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
    
        category_id = self.request.GET.get('category_id')

        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset
                

class ArticleViewSet(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(active=True)
        
        product_id = self.request.GET.get('product_id')

        if product_id is not None:
            queryset = queryset.filter(product_id=product_id)

        return queryset