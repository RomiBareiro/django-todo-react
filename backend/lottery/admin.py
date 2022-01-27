from django.contrib import admin
from .models import  Lottery
from .models import  ArgLottery
class LotteryAdmin(admin.ModelAdmin):
    list_display = ('id','timestamp', 
                    'numero1', 
                    'numero2', 
                    'numero3', 
                    'numero4', 
                    'numero5', 
                    'numero6', 
                    'numero7', 
                    'numero8', 
                    'numero9', 
                    'numero10', 
                    'numero11', 
                    'numero12', 
                    'numero13',
                   )

admin.site.register(Lottery, LotteryAdmin)
class ArgLotteryAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_sorteo',
                    'tipo_quiniela',
                    'fecha',
                    'timezone_type',
                    'timezone',
                    'letras',
                    'premios',
                    'pozo_proximo',
                    'numero1', 
                    'numero2', 
                    'numero3', 
                    'numero4', 
                    'numero5', 
                    'numero6', 
                    'numero7', 
                    'numero8', 
                    'numero9', 
                    'numero10', 
                    'numero11', 
                    'numero12', 
                    'numero13',
                    'numero14', 
                    'numero15', 
                    'numero16', 
                    'numero17',
                    'numero18', 
                    'numero19', 
                    'numero20', 
                   )
admin.site.register(ArgLottery, ArgLotteryAdmin)
