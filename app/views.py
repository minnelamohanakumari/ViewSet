from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from app.models import *
from app.serializers import *
from rest_framework.response import Response
class ProductData(ViewSet):
    def list(self,request,pk):
        PO=Product.objects.all()
        SD=Productserializer(PO,many=True)
        return Response(SD.data)

    def create(self,request,pk):
        SD=Productserializer(data=request.data)
        if SD.is_valid():
            SD.save()
            return Response({'message':'product data is created'})
        else:
            return Response({'message':'product is not created'})
    def retrieve(self,request,pk):
        PO=Product.objects.get(pk=pk)
        SD=Productserializer(PO)
        return Response(SD.data)

    def update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        SOD=Productserializer(PO,data=request.data)
        if SOD.is_valid():
            SOD.save()
            return Response({'message':'product is updated'})
        else:
            return Response({'message':'product is not updated'})

    def partial_update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        SOD=Productserializer(PO,data=request.data,partial=True)
        if SOD.is_valid():
            SOD.save()
            return Response({'message':'product is partial updated'})
        else:
            return Response({'message':'product is not updated-'})

    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'message':'product is deleted'})


