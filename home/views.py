from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Animal
from.serializers import AnimalSerializer
class AnimalView(APIView):
    
    def get(self, request):
        queryset=Animal.objects.all()
        serializer=AnimalSerializer(queryset, many=True)
        return Response({
               'status' : True,
               'message' : 'animal fetched with GET',
               'data' : serializer.data
        })
    
    def post(self, request):
        return Response({
               'status' : True,
               'message' : 'animal fetched with POST'
        })
        
    
    def put(self, request):
        return Response({
               'status' : True,
               'message' : 'animal fetched with PUT'
        })
        
    def patch(self, request):
        return Response({
               'status' : True,
               'message' : 'animal fetched with PATCH'
        })

class AnimalDetailView(APIView):
    def get (self, request, pk):
        try:
            queryset=Animal.objects.get(pk=pk)
            queryset.incrementViews()
            serializer=AnimalSerializer(queryset)
            
            
            
            return Response({
               'status' : True,
               'message' : 'animal fetched with GET',
               'data' : serializer.data
            })
            
        except Exception as e:
            print(e)
            
            return Response({
                'status': False,
                'message': "Something went wrong",
                'data' : {}
            })
            
        