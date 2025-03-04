from rest_framework.response import Response
from rest_framework import status
from .models import Products
from .serializers import ProductSerializers
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def products_list(request,format=None):
    if request.method == 'GET':
        prods = Products.objects.all()
        serializer = ProductSerializers(prods,many = True)
        return Response({'products ':serializer.data})
    
    if request.method == 'POST':
        serializer = ProductSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def products_details(request,id,format=None):
    try:
        prod = Products.objects.get(pk = id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = ProductSerializers(prod)
        return Response(serializers.data)
    elif request.method == 'PUT':
        serializers = ProductSerializers(prod,data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    