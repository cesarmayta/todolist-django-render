from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Tarea
from .serializers import TareaSerializer

class IndexView(APIView):
    
    def get(self,request):
        context = {
            'status':True,
            'content':'servidor activo'
        }
        return Response(context)
    
class TareaView(APIView):
    
    def get(self,request):
        data = Tarea.objects.all()
        ser_data = TareaSerializer(data,many=True)
        
        context = {
            'status':True,
            'content':ser_data.data
        }
        
        return Response(context)
    
    def post(self,request):
        ser_data = TareaSerializer(data=request.data)
        ser_data.is_valid(raise_exception=True)
        ser_data.save()
        
        #serializer = TareaSerializer(data)
        
        context = {
            'status':True,
            'content':ser_data.data
        }
        
        return Response(context)
    
class TareaDetailView(APIView):
    
    def get_object(self,pk):
        try:
            return Tarea.objects.get(pk=pk)
        except Tarea.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        data = self.get_object(pk)
        ser_data = TareaSerializer(data)
        context = {
            'status':True,
            'content':ser_data.data
        }
        
        return Response(context)
    
    def put(self,request,pk):
        data = self.get_object(pk)
        ser_data = TareaSerializer(data,data=request.data)
        
        if ser_data.is_valid():
            ser_data.save()
            context = {
                'status':True,
                'content':ser_data.data
            }
            return Response(context)
    
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        data = self.get_object(pk)
        data.estado = request.data['estado']
        data.save()
        
        ser_data = TareaSerializer(data)
        
        context = {
            'status':True,
            'content':ser_data.data
        }
        return Response(context)
    
    
    def delete(self,request,pk):
        data = self.get_object(pk)
        del_data = self.get_object(pk)
        ser_data = TareaSerializer(data)
        del_data.delete()
        
        context = {
                'status':True,
                'content':ser_data.data
            }
        
        return Response(context)
