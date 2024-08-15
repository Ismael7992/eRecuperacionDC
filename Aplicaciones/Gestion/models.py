from django.db import models

class Piloto(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=10)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    nombres = models.CharField(max_length=100)
    email = models.EmailField()
    numero_celular = models.CharField(max_length=15)
    foto_carnet = models.FileField(upload_to='fotos_carnet/')
    hoja_vida_pdf = models.FileField(upload_to='hojas_vida/')
    def __str__(self):
        fila= "{0}: {1}-{2}-{3}-{4}-{5}-{6}-{7}-{8}"
        return fila.format(self.id,self.dni,self.primer_apellido,self.segundo_apellido,self.nombres,self.email,self.numero_celular,self.foto_carnet,self.hoja_vida_pdf)


class Avion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    numero_matricula = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    ano_creacion = models.IntegerField()
    fotografia = models.FileField(upload_to='fotografias/')
    piloto = models.ForeignKey(Piloto, null=True,on_delete=models.SET_NULL)
    def __str__(self):
        fila= "{0}: {1}-{2}-{3}-{4}-{5}-{6}-{7}"
        return fila.format(self.id,self.nombre,self.marca,self.numero_matricula,self.capacidad,self.ano_creacion,self.fotografia,self.piloto)
