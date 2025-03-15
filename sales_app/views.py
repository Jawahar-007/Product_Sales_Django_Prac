from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Products,Orders,Blog,Comment
from .serializers import ProductSerializers,OrdersSerializers,BlogSerializers,CommentSerializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins,generics,viewsets
from .paginations import CustomPagination
from .filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.
# @api_view(['GET','POST'])
# def products_list(request,format=None):
#     if request.method == 'GET':
#         prods = Products.objects.all()
#         serializer = ProductSerializers(prods,many = True)
#         return Response({'products ':serializer.data})
    
#     if request.method == 'POST':
#         serializer = ProductSerializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = status.HTTP_201_CREATED)
        
# @api_view(['GET','PUT','DELETE'])
# def products_details(request,id,format=None):
#     try:
#         prod = Products.objects.get(pk = id)
#     except Products.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializers = ProductSerializers(prod)
#         return Response(serializers.data)
#     elif request.method == 'PUT':
#         serializers = ProductSerializers(prod,data= request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         prod.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# #mixins
# class OrdersList(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializers
    
#     def get(self, request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)
    
# class OrderDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializers

#     def get(self,request,pk):
#         return self.retrieve(request,pk)
    
#     def put(self,request,pk):
#         return self.update(request,pk)
    
#     def delete(self,request,pk):
#         return self.destroy(request,pk)

# #Generics   
# class OrderGenericsList(generics.ListCreateAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializers

# class OrderGenericDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializers
#     lookup_field = "pk"

# class OrderViewSet(viewsets.ViewSet):
#     def list(self,request):
#         queryset = Orders.objects.all()
#         serializer = OrdersSerializers(queryset , many=True)
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer = OrdersSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)  

#     def retrieve(self,request,pk=None):
#         ord = get_object_or_404(Orders,pk=pk)      
#         serializer = OrdersSerializers(ord)
#         return Response(serializer.data,status= status.HTTP_200_OK)                                            # except Orders.DoesNotExist:
                                            
#     def update(self,request,pk=None):
#         ord = get_object_or_404(Orders,pk=pk)
#         serializer = OrdersSerializers(ord, data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)

#     def delete(self,request,id):
#         ord = get_object_or_404(Orders,pk=id)
#         ord.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
     
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializers

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializers

class Products_View(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializers
    pagination_class = CustomPagination
    filterset_class = ProductFilter

class Products_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'id'

class Order_View(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers    

class Blog_View(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['blog_title','blog_body']
    ordering_fields = ['id','blog_title']

class Blog_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    lookup_field = 'id'


class Comment_view(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers