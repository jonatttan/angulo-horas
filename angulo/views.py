from django.shortcuts import render
from .models import Angulo
from .serializers import AnguloSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

def insert_db(h, m):
    if h < 1 or h > 12:
        return "Digite hora entre 1 e 12"
    if m < 0 or m > 59:
        return "Digite minuto entre 1 e 59"
        
    hour = h
    minute = m
    m = 11 * minute
    h = 60 * hour
    angle = (m-h)/2
    if angle < 0:
        angle = angle *-1
        angle = 360 - angle
    newAngle = Angulo(hour=hour, minute=minute, angle=angle)
    newAngle.save()
    return ("Não existe o ângulo consultado, cadastrando... Atualize a página")

def query_db(h,m):
    angulos = Angulo.objects.filter(hour=h)
    angulos = angulos.get(minute=m)
    serializer = AnguloSerializer(angulos, many=False)
    return serializer.data

class AngleCalcHour(APIView):
    def get(self, request, h, format=None):
        get_data = request.query_params
        try:
            mesage = query_db(h, 0)
        except Angulo.DoesNotExist:
            mesage = insert_db(h, 0)                
        finally:
            return Response(mesage)

class AnguloCalcHourMinute(APIView):
    def get(self, request, h, m, format=None):
        if type(h) == int:
            get_data = request.query_params
            try:
                mesage = query_db(h, m)
            except Angulo.DoesNotExist:
                mesage = insert_db(h, m)
            finally:
                return Response(mesage)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnguloList(APIView):
    def get(self, request, format=None):
        get_data = request.query_params
        angulos = Angulo.objects.all()
        serializer = AnguloSerializer(angulos, many=True)
        return Response(serializer.data)

