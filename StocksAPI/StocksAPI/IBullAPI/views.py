from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Trade
from . serializers import TradeSerializer

# Create your views here.
class TradeList(APIView):
    def get(self, request):
        Trades=Trade.objects.all()
        serializer = TradeSerializer(Trades, many=True)
        return Response(serializer.data)


        