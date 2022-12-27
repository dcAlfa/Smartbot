from django.urls import path
from .views import *


urlpatterns = [
    path('bot-users', BotUserApi.as_view(), name="bot-users"),
    path('profillar', ProfilApi.as_view(), name="profillar"),
    path('hududlar', HududApi.as_view(), name="hududlar"),
    path('shaharlar', ShaharApi.as_view(), name="shaharlar"),
]