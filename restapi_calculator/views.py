from django import urls
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

def index():
    return 0

@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def sakti(request):
    try:
        hitung = eval(request.POST['inputan'])
        return Response({
            'status':'success',
            'data':{
                    'inputan': request.POST['inputan'],
                    'result':hitung
                    }
                }
            )
    except Exception as gagal:
        return Response({'status':'error', 'message':str(gagal)})
        
def tambah(request):
    try:
        input1 = float(request.POST['input1'])
        input2 = float(request.POST['input2'])
        answer = input1 + input2
        return Response({
            'status':'success','data':{'result':answer}}
            )
    except Exception as gagal:
        return Response({'status':'error', 'message':str(gagal)})


