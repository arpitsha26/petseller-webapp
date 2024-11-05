from rest_framework.views import APIView
from rest_framework.response import Response


class AnimalView(APIView):
    
    def get(self, request):
        return Response({
               'status' : True,
               'message' : 'animal fetched with GET'
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
        