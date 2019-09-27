from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.parsers import FileUploadParser
from deeplearn.serializers import deepSerializer
from deeplearn.models import deep
from deeplearn import firstDL

# Create your views here.
class deepUploadView(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
        deep_serializer = deepSerializer(data=request.data)
        if deep_serializer.is_valid():
            deep_serializer.save("tmp.jpg")
            return Response(deep_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(deep_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class deepViewSet(viewsets.ModelViewSet):
    parser_class = (FileUploadParser,)        
    queryset = deep.objects.all().order_by('-id')
    serializer_class = deepSerializer
    def create(self, request, *args, **kwargs):
        super(viewsets.ModelViewSet, self).create(request, *args, **kwargs)
        ob = deep.objects.latest('id')
        y = firstDL.pred(ob)
        return Response({"status": "Success", "class": y, 'tmp': args}) 