from django.db import models

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name

class Practical(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    aim = models.CharField(max_length=300)
    objectives = models.TextField(max_length=5000)
    additional = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name



