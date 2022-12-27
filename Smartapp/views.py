from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView


class BotUserApi(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSer

class ProfilApi(ListCreateAPIView):
    queryset = Profil.objects.all()
    serializer_class = ProfilSer

class HududApi(ListCreateAPIView):
    queryset = Hudud.objects.all()
    serializer_class = HududSer

class ShaharApi(ListCreateAPIView):
    queryset = Shahar.objects.all()
    serializer_class = ShaharSer
