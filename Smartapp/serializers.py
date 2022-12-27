from .models import *
from rest_framework.serializers import ModelSerializer

class BotUserSer(ModelSerializer):
    class Meta:
        model = BotUser
        fields = "__all__"

class ProfilSer(ModelSerializer):
    class Meta:
        model = Profil
        fields = "__all__"

class HududSer(ModelSerializer):
    class Meta:
        model = Hudud
        fields = "__all__"

class ShaharSer(ModelSerializer):
    class Meta:
        model = Shahar
        fields = "__all__"