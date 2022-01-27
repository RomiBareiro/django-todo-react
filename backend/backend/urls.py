from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views as todoViews
from lottery.views import LotteryViewes
from lottery.models import Lottery

router = routers.DefaultRouter()
router.register(r'todos', todoViews.TodoView, 'todo')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('lottery_views/', LotteryViewes.as_view()),
    
]