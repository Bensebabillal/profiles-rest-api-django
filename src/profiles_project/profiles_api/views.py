from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

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