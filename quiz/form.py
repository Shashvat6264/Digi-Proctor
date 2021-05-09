from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from .models import *

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['quizName','noOfQns']

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['questionName', 'questionDesc', 'questionQuiz']
        widgets = {
            'questionDesc': Textarea()
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'type', 'username')