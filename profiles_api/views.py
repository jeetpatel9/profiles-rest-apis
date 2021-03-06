from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


# Create your views here.

class HelloAPIView(APIView):

    serializers_class = serializers.HelloSerializer

    def get(self, request, formate=None):

        an_apiview = [
            'ahskbajc',
            'ads',
            'ahskbajc',
            'ads',
            'ahskbajc',
            'ads',
        ]

        return Response({
        'message' : 'Hello',
        'an_apiview' : an_apiview
        })

    def post(self, request):
        serializers = self.serializers_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):

    serializers_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'ahskbajc',
            'ads',
            'ahskbajc',
            'ads',
            'ahskbajc',
            'ads',
        ]

        return Response({'message':'Hello', 'a_viewset': a_viewset})

    def create(self, request):

        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'message':'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'message': 'DELETE'})
