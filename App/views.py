from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializer import FileListSerializer,FileSerializer
from .models import Folder,Files
from rest_framework.views import APIView
from django.http import HttpResponse,StreamingHttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def download(request,uid):
    return render(request,'download.html',context={'uid': uid})    

class HandleFileUpload(APIView):
    
    def post(self,request):
        try:
            data=request.data
            serializer=FileListSerializer(data=data)
        except:
            return Response({"status" : "Wrong Input type."})

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : 200,
                'message':'File Uploaded Successfully',
                'data' : serializer.data,
            })

        return Response({
            'status' : 400,
            'message':'Something Went Wrong',
            'data' : serializer.errors,
        })