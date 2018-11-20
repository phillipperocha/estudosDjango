from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=150)
    idade = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2) # vai ser máximo de 5 dígitos, sendo 2 casas depois da vírgula
    bio = models.TextField() # vai ser um text Area
    photo = models.ImageField(upload_to='pacientes_photos', null=True, blank=True) #Serve se você quiser salvar essa imagem em uma pasta especial dentro da pasta de media


    def __str__(self):
        return self.nome + " " + self.sobrenome