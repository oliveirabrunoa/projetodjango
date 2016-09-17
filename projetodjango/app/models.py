from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Pessoa(models.Model):
    id_rede = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80, blank=False, null=False)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
