from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class HelloAPIView(APIView):
    """docstring for HelloAPIView."""

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
