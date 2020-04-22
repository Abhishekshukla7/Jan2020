from django.db import models

class institute(models.Model):
    Name = models.CharField(max_length=200,null=True, blank=True)
    Contact = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.Name

class Students(models.Model):
    ins= models.ForeignKey(institute, on_delete=models.SET_NULL, null=True)
    Name = models.CharField(max_length=100)
    Number = models.IntegerField()
    Email = models.EmailField()
    Address = models.TextField()
    College = models.CharField(max_length=100, null=True)

class List(models.Model):
    Name = models.CharField(max_length=100)
    Number = models.IntegerField()
    Email = models.EmailField()

class Subject(models.Model):
    Name = models.CharField(max_length=100)
    Teacher = models.CharField(max_length=100)
    SubjectCode = models.IntegerField()