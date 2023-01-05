from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    pontuacao = models.IntegerField(blank=True, null=True)
    habilitado = models.BooleanField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome





class Computadore(models.Model):
    dono_do_pc = models.CharField(max_length=100)
    processador = models.CharField(max_length=100)
    placa_mae = models.CharField(max_length=100)
    placa_de_video = models.CharField(max_length=100)
    memoria_ram = models.CharField(max_length=100)
    possui_ssd_ou_hd = models.BooleanField(blank=True, null=True)
    quantos_ssd_ou_hd = models.IntegerField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.dono_do_pc

   


    
