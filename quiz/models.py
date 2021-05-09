from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

# User Type models
class User(AbstractUser):

    class Types(models.TextChoices):
        PROF = "Prof"
        STUDENT = "STUDENT"
    
    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.STUDENT)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("user:detail", kwargs={"username": self.username})
    
class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STUDENT)

class ProfManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.PROF)


class Student(User):
    objects = StudentManager()

    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.STUDENT
        return super().save(*args, **kwargs)

class Prof(User):
    objects = ProfManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.PROF
        return super().save(*args, **kwargs)

# Models for Implementation of Quiz Portal
class Quiz(models.Model):
    quizID = models.AutoField(primary_key=True)
    quizName = models.CharField(max_length=20, verbose_name="Quiz Name: ")
    noOfQns = models.IntegerField(verbose_name="Number of Questions: ")

    def __str__(self):
        return self.quizName

class Question(models.Model):
    questionID = models.AutoField(primary_key=True)
    questionName = models.CharField(max_length=200, verbose_name="Question Name: ")
    questionDesc = models.CharField(max_length=400, verbose_name="Question Decription: ")
    questionQuiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="Quiz: ")

    def __str__(self):
        return self.questionName

class ResponseQuiz(models.Model):
    id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Response(models.Model):
    id = models.AutoField(primary_key=True)
    response = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    responseQuiz = models.ForeignKey(ResponseQuiz, on_delete=models.CASCADE)
    windowChange = models.IntegerField()
    windowAwayTime = models.IntegerField()

    def __str__(self):
        return str(self.id)


