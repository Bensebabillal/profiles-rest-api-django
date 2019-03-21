from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.


serializer_class =serializers.HelloSerializer

class HelloApiView(APIView):
    """Teste API View"""

    def get (self,request,format=None):
        """return a liste of APIView features"""

        an_apiview =[
            'used HTTP methode as function 9get,post,patch,put, delete)',
            'it is similar to a trditional Django view',
            'Gives you the most control over your logic',
            'is mapped manually to URLs',
        ]

        return Response({'message': 'Hello! Word','an_apiview' : an_apiview })

    def post(self, request):
        """create hello message with our name. """

        serializer= serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name= serializer.data.get('name')
            message ='hello {0}'.format(name)
            return Response ({'message':message})

        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """handle updating an object"""

        return Response({'methode':'put'})

    def patch(self,request,pk=None):
        """Patch request, only updates fields provided in the request ."""

        return Response({'methode':'patch'})

    def delete(self,request,pk=None):
        """Delete an object"""

        return Response({'methode':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""
    def list(self,request):
        """return a list of APIView features."""
        a_viewset =[
            'uses action (list, creat , retrieve , update, partial_update)',
            'automatically maps to URLs using Routers',
            'provides more functionnality with less code.',
        ]

        return Response({'message':'hello!','a_viewset':a_viewset})
