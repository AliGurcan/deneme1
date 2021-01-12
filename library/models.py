from django.db import models


class Academician(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return "%s" % self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    academician = models.ForeignKey(Academician, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class LectureNotes(models.Model):
    name = models.CharField(max_length=30)
    academician = models.ForeignKey(Academician, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='lnotes/pdfs/', null=True, blank=True)
    image = models.ImageField(upload_to='lnotes/images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Student(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class StudentNotes(models.Model):
    name = models.CharField(max_length=30)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='snotes/pdfs/', null=True, blank=True)
    image = models.ImageField(upload_to='snotes/images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']