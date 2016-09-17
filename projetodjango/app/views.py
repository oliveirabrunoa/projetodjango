from django.shortcuts import render
from django.shortcuts import render
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from .models import *


# Create your views here.

class GetAllPessoas(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        redes = Pessoa.objects.all()
        # paginator = PageNumberPagination()
        # result_page = paginator.paginate_queryset(redes, request)
        serializer = PessoaSeralizer(redes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PessoaSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)