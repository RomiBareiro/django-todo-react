
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework import status
from .services import get_lotteries_payed_api

from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .serializers import ArgLotterySerializer
from .models import  ArgLottery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

    queryset = get_lotteries_payed_api()
    def translate_queryset(self):
        self.quiniela_data = self.parse_queryset(self.tipo_quiniela, self.queryset)
        self.sorteo_data = self.parse_queryset(self.nombre_sorteo, self.quiniela_data)
        self.numbers_dict_list= self.parse_queryset(self.numbers_name, self.sorteo_data[0])
        self.date_dict = self.parse_queryset(self.date_name, self.sorteo_data[0])
        self.letras = self.parse_queryset("letras", self.sorteo_data[0])
        self.premios = self.parse_queryset("premios", self.sorteo_data[0])
        self.pozo_proximo = self.parse_queryset("pozo_proximo", self.sorteo_data[0])

        if len(self.premios) == 0:
            self.premios = ""
        if self.pozo_proximo is None:
            self.pozo_proximo = ""
        
        self.parse_numeros(self.tipo_quiniela)
        self.parse_date(self.tipo_quiniela)
        

    def parse_queryset(self, quiniela_type_name, queryset):
        query_quiniela = queryset.get(quiniela_type_name)
        return query_quiniela

    def parse_date(self, quiniela_type_name ):
        if quiniela_type_name == self.tipo_quiniela:
            self.date = self.date_dict.get('date')
            self.timezone_type = self.date_dict.get('timezone_type')
            self.timezone = self.date_dict.get('timezone')
        else :
            return

    def parse_numeros(self, quiniela_type_name ):
        if quiniela_type_name == self.tipo_quiniela:
                for i in range(0,20):
                    self.numeros[i+1] = self.numbers_dict_list[i].get(str(i+1))
        else :
            return

lottery_object = Lottery('Quiniela Nacional', 'Primera')

class SerializedData():
    serialized_dict = {}
    def __init__(self, quiniela):
        self.lottery_dict = {
        'tipo_quiniela' : quiniela.tipo_quiniela ,
        'nombre_sorteo' : quiniela.nombre_sorteo,
        'fecha' :  quiniela.date,
        'timezone_type' : quiniela.timezone_type,
        'timezone' : quiniela.timezone,
        'letras' : quiniela.letras,
        'premios' : quiniela.premios,
        'pozo_proximo' : quiniela.pozo_proximo,
        'numero1' : quiniela.numeros[1],
        'numero2' : quiniela.numeros[2],
        'numero3' : quiniela.numeros[3],
        'numero4' : quiniela.numeros[4],
        'numero5' : quiniela.numeros[5],
        'numero6' : quiniela.numeros[6],
        'numero7' : quiniela.numeros[7],
        'numero8' : quiniela.numeros[8],
        'numero9' : quiniela.numeros[9],
        'numero10' : quiniela.numeros[10],
        'numero11' : quiniela.numeros[11],
        'numero12' : quiniela.numeros[12],
        'numero13' : quiniela.numeros[13],
        'numero14' : quiniela.numeros[14],
        'numero15' : quiniela.numeros[15],
        'numero16' : quiniela.numeros[16],
        'numero17' : quiniela.numeros[17],
        'numero18' : quiniela.numeros[18],
        'numero19' : quiniela.numeros[19],
        'numero20' : quiniela.numeros[20],
        }



@api_view(['GET', 'POST'])
def lotteries_list(request):
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        lottery = ArgLottery.objects.all()
        page = request.GET.get('page', 5)
        paginator = Paginator(lottery, 1)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = ArgLotterySerializer(data ,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/lotteries/?page=' + str(nextPage), 'prevlink': '/api/lotteries/?page=' + str(previousPage)})

    elif request.method == 'POST':
        lottery_object.translate_queryset()
        translated_data = SerializedData(lottery_object)
        serializer = ArgLotterySerializer(data=translated_data.lottery_dict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def lotteries_detail(request, id):
    try:
        lottery = get_object_or_404(ArgLottery, pk=id)
    except ArgLottery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArgLotterySerializer(lottery,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArgLotterySerializer(lottery, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lottery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
