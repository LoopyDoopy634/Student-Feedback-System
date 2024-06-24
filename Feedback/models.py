from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return f"Feedback by {self.student} for {self.faculty}"
