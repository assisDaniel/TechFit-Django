from django.db import models


# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    cpf = models.CharField(max_length=14, unique=True, null=False, blank=False)
    senha = models.CharField(max_length=30, null=False, blank=False)
    telefone = models.CharField(max_length=16, null=False, blank=False)
    dt_nascimento = models.DateField(null=False, blank=False)
    pdf_avaliacao = models.FileField(null=True, blank=True, upload_to='')
    pdf_ficha = models.FileField(null=True, blank=True, upload_to='')
    superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
