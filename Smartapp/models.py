from django.db import models


class BotUser(models.Model):
    user_id = models.CharField(max_length=120, unique=True)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)



class Hudud(models.Model):
    name = models.CharField(max_length=255, default="Farg'ona")

    def __str__(self):
        return str(self.name)


class Shahar(models.Model):
    name = models.CharField(max_length=255, default="Farg'ona")
    hudud = models.ForeignKey(Hudud, models.CASCADE)
    def __str__(self):
        return str(self.name)

class Profil(models.Model):
    user_id = models.CharField(max_length=255,unique=True)
    fulname = models.CharField(max_length=255)
    lavozim = models.CharField(max_length=200)
    tel = models.CharField(max_length=30)
    shahar = models.ForeignKey(Shahar, models.CASCADE)
    def __str__(self):
        return str(self.fulname)


