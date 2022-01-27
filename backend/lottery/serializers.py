from rest_framework import serializers
from .models import ArgLottery, Lottery

class LotterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lottery
        fields = ('timestamp','status', 'numero1', 'numero2', 'numero3',
                    'numero4', 'numero5', 'numero6','numero7', 'numero8', 'numero9',
                    'numero10', 'numero11', 'numero12', 
                    'fraseSorteoPDF','fraseListaPDF','listaPDF','urlAudio','error')

class ArgLotterySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArgLottery
        fields = '__all__'

                         