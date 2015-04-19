from django.db import models
from django.core.exceptions import ValidationError


class Mecz(models.Model):
    opis = models.CharField(max_length = 100)
    wynika = models.IntegerField()
    wynikb = models.IntegerField()


class Zaklad(models.Model):
    kto = models.CharField(max_length = 100)
    mecz = models.ForeignKey(Mecz)
    wynika = models.IntegerField()
    wynikb = models.IntegerField()

    def clean(self):
        innezaklady = Zaklad.objects.all()
        for innyzaklad in innezaklady:
            if self.id != innyzaklad.id and self.kto == innyzaklad.kto and self.mecz == innyzaklad.mecz:
                raise ValidationError('Dana osoba juz obstawiala dany mecz.')
