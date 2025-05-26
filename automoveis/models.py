from django.db import models

# Create your models here.

class Automovel(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano_fabricacao = models.IntegerField()
    cor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2,)
    imagem = models.ImageField(upload_to='media/', blank=True, null=True)
    class Meta:
        abstract = True

class Carro(Automovel):
    COMBUSTIVEL = {
        ('Gasolina', 'Gasolina'),
        ('Etanol', 'Etanol'),
        ('Diesel', 'Diesel'),
        ('Flex', 'Flex'),
        ('Eletrico', 'Eletrico'),
        ('Hibrido', 'Hibrido'),
    }
    TIPO_CARRO = {
        ('Hatch', 'Hatch'),
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Picape', 'Picape'),
        ('Coupe', 'Coupé'),
        ('Conversivel', 'Conversível'),
    }
    tipo_combustivel = models.CharField(max_length=50, choices=COMBUSTIVEL, default='Gasolina')
    numero_portas = models.IntegerField()
    quilometragem = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_do_carro = models.CharField(max_length=50, choices=TIPO_CARRO, default='Sedan')

    def __str__(self):
        return f'{self.modelo} | {self.marca}'

class Moto(Automovel):
    COMBUSTIVEL = {
        ('Gasolina', 'Gasolina'),
        ('Etanol', 'Etanol'),
        ('Eletrico', 'Eletrico'),
    }
    tipo_combustivel = models.CharField(max_length=50, choices=COMBUSTIVEL, default='Gasolina')
    cilindrada = models.IntegerField()

    def __str__(self):
        return f'{self.modelo} | {self.marca}'

class Caminhao(Automovel):
    tipo_eixo = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.modelo} | {self.marca}'