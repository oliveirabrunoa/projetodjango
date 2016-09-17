from rest_framework import serializers
from .models import *


class PessoaSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'