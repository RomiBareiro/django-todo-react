from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from todo import views as todoViews

from lottery.views import lotteries_detail, lotteries_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/lotteries/', lotteries_list),
    path('api/lotteries_detail/<int:id>/', lotteries_detail),
]