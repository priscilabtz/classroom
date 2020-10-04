from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    activity = models.CharField(max_length=255)
    statement = models.CharField(max_length=255)
    answer = ArrayField(models.CharField(max_length=64))
    options = ArrayField(models.CharField(max_length=64))
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
