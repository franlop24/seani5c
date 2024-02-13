from django.db import models

# Create your models here.
class Module(models.Model):
    name = models.CharField(
        verbose_name = "Nombre",
        max_length=100)
    description = models.CharField(
        verbose_name = 'Descripción',
        max_length = 200)


class Question(models.Model):
    module = models.ForeignKey(Module, on_delete = models.CASCADE)
    text_question = models.CharField(
        verbose_name = 'Texto de la Pregunta',
        max_length=200, null = True)
    text_image = models.ImageField(
        verbose_name = 'Imagen de la Pregunta',
        upload_to='questions', null = True)
    answer1 = models.CharField(
            verbose_name = 'Respuesta A',
            max_length=200)
    answer2 = models.CharField(
            verbose_name = 'Respuesta B',
            max_length=200)
    answer3 = models.CharField(
            verbose_name = 'Respuesta C',
            max_length=200, null = True)
    answer4 = models.CharField(
            verbose_name = 'Respuesta D',
            max_length=200, null = True)
    correct = models.CharField(
            verbose_name = 'Respuesta Correcta', 
            max_length = 5)
