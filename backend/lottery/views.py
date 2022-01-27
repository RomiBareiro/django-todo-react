from logging import Logger
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import get_lotteries, get_lotteries_payed_api
from rest_framework.decorators import action
from rest_framework.views import APIView

from .serializers import ArgLotterySerializer, LotterySerializer
from .models import  ArgLottery, Lottery

class LotteryViewes (APIView):
    class AdditionalInfo():
        letras = ()
        premios = ()
        pozo_proximo = ()
    
    class numbers():
        numbers_name = 'numeros'
        numbers_dict_list = {}
        numeros = {}
    class date():
        date_name = 'fecha'
        date = ""
        timezone_type =""
        timezone = ""
        date_dict = {}

    class Sorteo(AdditionalInfo, numbers, date):
        sorteo_data = {}
        nombre_sorteo = ""
        def __init__(self, name_sorteo):
            self.nombre_sorteo = name_sorteo

    class Quiniela(Sorteo):
        quiniela_data = {}
        tipo_quiniela = ""
        def __init__(self, quiniela_name, sorteo_name):
            self.tipo_quiniela = quiniela_name
            super().__init__(sorteo_name)

    class Lottery(Quiniela):
        def __init__(self, quiniela_name, sorteo_name):
            self.tipo_quiniela = quiniela_name
            super().__init__(self.tipo_quiniela, sorteo_name)

    class SerializedData():
        serialized_dict = {}
        def __init__(self, quiniela_nacional):
            self.lottery_dict = {
            'tipo_quiniela' : quiniela_nacional.tipo_quiniela ,
            'nombre_sorteo' : quiniela_nacional.nombre_sorteo,
            'fecha' :  quiniela_nacional.date,
            'timezone_type' : quiniela_nacional.timezone_type,
            'timezone' : quiniela_nacional.timezone,
            'letras' : quiniela_nacional.letras,
            'premios' : quiniela_nacional.premios,
            'pozo_proximo' : quiniela_nacional.pozo_proximo,
            'numero1' : quiniela_nacional.numeros[1],
            'numero2' : quiniela_nacional.numeros[2],
            'numero3' : quiniela_nacional.numeros[3],
            'numero4' : quiniela_nacional.numeros[4],
            'numero5' : quiniela_nacional.numeros[5],
            'numero6' : quiniela_nacional.numeros[6],
            'numero7' : quiniela_nacional.numeros[7],
            'numero8' : quiniela_nacional.numeros[8],
            'numero9' : quiniela_nacional.numeros[9],
            'numero10' : quiniela_nacional.numeros[10],
            'numero11' : quiniela_nacional.numeros[11],
            'numero12' : quiniela_nacional.numeros[12],
            'numero13' : quiniela_nacional.numeros[13],
            'numero14' : quiniela_nacional.numeros[14],
            'numero15' : quiniela_nacional.numeros[15],
            'numero16' : quiniela_nacional.numeros[16],
            'numero17' : quiniela_nacional.numeros[17],
            'numero18' : quiniela_nacional.numeros[18],
            'numero19' : quiniela_nacional.numeros[19],
            'numero20' : quiniela_nacional.numeros[20],
            }
            
    lottery_object = Lottery('Quiniela Neuquen', 'El Primero')
    queryset = get_lotteries_payed_api()
    def translate_queryset(self):
        self.lottery_object.quiniela_data = self.parse_queryset(self.lottery_object.tipo_quiniela, self.queryset)
        self.lottery_object.sorteo_data = self.parse_queryset(self.lottery_object.nombre_sorteo, self.lottery_object.quiniela_data)
        self.lottery_object.numbers_dict_list= self.parse_queryset(self.lottery_object.numbers_name, self.lottery_object.sorteo_data[0])
        self.lottery_object.date_dict = self.parse_queryset(self.lottery_object.date_name, self.lottery_object.sorteo_data[0])
        self.lottery_object.letras = self.parse_queryset("letras", self.lottery_object.sorteo_data[0])
        self.lottery_object.premios = self.parse_queryset("premios", self.lottery_object.sorteo_data[0])
        self.lottery_object.pozo_proximo = self.parse_queryset("pozo_proximo", self.lottery_object.sorteo_data[0])
        if len(self.lottery_object.premios) == 0:
            self.lottery_object.premios = ""
        if self.lottery_object.pozo_proximo is None:
            self.lottery_object.pozo_proximo = ""
        
        self.parse_numeros(self.lottery_object.tipo_quiniela)
        self.parse_date(self.lottery_object.tipo_quiniela)
        return None

    def parse_queryset(self, quiniela_type_name, queryset):
        query_quiniela = queryset.get(quiniela_type_name)
        return query_quiniela
    
    def parse_date(self, quiniela_type_name ):
        if quiniela_type_name == self.lottery_object.tipo_quiniela:
            self.lottery_object.date = self.lottery_object.date_dict.get('date')
            self.lottery_object.timezone_type = self.lottery_object.date_dict.get('timezone_type')
            self.lottery_object.timezone = self.lottery_object.date_dict.get('timezone')
        else :
            return
        return 

    def parse_numeros(self, quiniela_type_name ):
        if quiniela_type_name == self.lottery_object.tipo_quiniela:
                for i in range(0,20):
                    self.lottery_object.numeros[i+1] = self.lottery_object.numbers_dict_list[i].get(str(i+1))
        else :
            return

    def get(self,request):
        lottery = ArgLottery.objects.all()
        serializer = ArgLotterySerializer(data=lottery,context={'request': request} ,many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'data': serializer.data })

    
    def post(self, request):  
        self.translate_queryset()
        serializer = ArgLotterySerializer(data=self.SerializedData(self.lottery_object).lottery_dict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def options(self, request):  
        return
