from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .form import *
import json
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout

# Create your views here.

# Functions for Selectivity
def student_check(user):
    return user.type == User.Types.STUDENT

def prof_check(user):
    return user.type == User.Types.PROF

def index(request):
    template = loader.get_template('quiz/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


# Views for the students
@login_required
@user_passes_test(student_check, login_url='/quiz/login')
def all_quizes(request):
    quizzes = Quiz.objects.all()
    template = loader.get_template('quiz/all_quizzes.html')
    context = {
        "quizzes": quizzes,
    }
    return HttpResponse(template.render(context, request))

@login_required
@user_passes_test(student_check, login_url='/quiz/login')
def quiz_start(request, quizID):
    current_user = request.user
    quiz = Quiz.objects.get(pk=quizID)
    questions = Question.objects.filter(questionQuiz__quizID = quizID)
    numOfQns = len(questions)

    responseQuizStart = ResponseQuiz(quiz=quiz, student=current_user);
    responseQuizStart.save()

    template = loader.get_template('quiz/quiz_start.html')
    context = {
        "quiz": quiz,
        "numOfQns": numOfQns,
        "nextqn": questions[0].questionID,
        "responseID": responseQuizStart.id,
    }
    return HttpResponse(template.render(context, request))

@login_required
@user_passes_test(student_check, login_url='/quiz/login')
def displayquizqn(request, quizID, questionID, responseID):
    quiz = Quiz.objects.get(pk=quizID)
    question = Question.objects.get(pk=questionID)
    questions = list(Question.objects.filter(questionQuiz__quizID = quizID))
    responseQuiz = ResponseQuiz.objects.get(pk=responseID)

    if request.method == 'POST':
        JSONresponse = json.loads(request.body)
        print(JSONresponse)
        response_rec = Response(
            response=JSONresponse['answer'], 
            question=question, 
            responseQuiz=responseQuiz, 
            windowChange=JSONresponse['windowChange'], 
            windowAwayTime=JSONresponse['windowTime']
        );
        response_rec.save()

    current_index = questions.index(question)
    nextQn = questions[current_index+1].questionID if (current_index<len(questions)-1) else None
        
    template = loader.get_template('quiz/questionDisplay.html')
    context = {
        "question": question,
        "quiz": quiz,
        "nextQn": nextQn,
        "responseID": responseID
    }
    return HttpResponse(template.render(context, request))

@login_required
@user_passes_test(student_check, login_url='/quiz/login')
def quizOver(request):
    template = loader.get_template('quiz/quiz_over.html')
    return HttpResponse(template.render({}, request))


# Views for the professor
@login_required
@user_passes_test(prof_check, login_url='/quiz/login')
def createQuiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            q = Quiz()
            q.quizName = form.cleaned_data['quizName']
            q.noOfQns = form.cleaned_data['noOfQns']
            q.save()
            return HttpResponse("Thanks")
    else:
        form = QuizForm()
        template = loader.get_template('quiz/quizForm.html')
        return HttpResponse(template.render({'form': form, 'formname': "QUIZ"}, request))

@login_required
@user_passes_test(prof_check, login_url='/quiz/login')
def createQuestion(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = Question()
            q.questionName = form.cleaned_data['questionName']
            q.questionDesc = form.cleaned_data['questionDesc']
            q.questionQuiz = form.cleaned_data['questionQuiz']
            q.save()
            return HttpResponse("Thanks")
    else:
        form = QuestionForm()
        template = loader.get_template('quiz/quizForm.html')
        return HttpResponse(template.render({'form': form, 'formname': "QUESTION"}, request))

@login_required
@user_passes_test(prof_check, login_url='/quiz/login')
def showQuiz(request):
    quizzes = Quiz.objects.all()
    template = loader.get_template('quiz/prof_quizzes.html')
    context = {
        "quizzes": quizzes,
    }
    return HttpResponse(template.render(context, request))

@login_required
@user_passes_test(prof_check, login_url='/quiz/login')
def showResponses(request, quizID):
    responseQuizzes = ResponseQuiz.objects.filter(quiz__quizID = quizID)
    quiz = Quiz.objects.get(pk=quizID)
    template = loader.get_template('quiz/showResponseQuiz.html')
    return HttpResponse(template.render({'responses': responseQuizzes, 'quiz': quiz}, request))

@login_required
@user_passes_test(prof_check, login_url='/quiz/login')
def showAResponse(request, quizID, reponseQuizID):
    responseQuiz = ResponseQuiz.objects.get(pk=reponseQuizID)
    responses = Response.objects.filter(responseQuiz__pk = reponseQuizID)
    template = loader.get_template('quiz/showresponse.html')
    return HttpResponse(template.render({'responses': responses, 'student': responseQuiz.student}, request))


# Views for Login
@csrf_protect
def registerView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['type'] == User.Types.STUDENT:
                s = Student()
                s.username = form.cleaned_data['username']
                s.email = form.cleaned_data['email']
                s.set_password(form.cleaned_data['password1'])
                s.type = form.cleaned_data['type']
                s.save()
            if form.cleaned_data['type'] == User.Types.PROF:
                s = Prof()
                s.username = form.cleaned_data['username']
                s.email = form.cleaned_data['email']
                s.set_password(form.cleaned_data['password1'])
                s.type = form.cleaned_data['type']
                s.save()
            return redirect('login_url')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


@login_required(login_url='/quiz/login')
def dashboardRedirect(request):
    current_user = request.user
    if current_user.type == User.Types.STUDENT:
        return redirect('StudentHome')
    elif current_user.type == User.Types.PROF:
        return redirect('ProfHome')

@login_required
@user_passes_test(student_check, login_url='/quiz/login')
def StudentHome(request):
    current_user = request.user
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/studenthome.html', {'user': current_user, 'quizzes': quizzes})

@login_required
@user_passes_test(prof_check, login_url='/quiz/login')
def ProfHome(request):
    current_user = request.user
    return render(request, 'quiz/profhome.html', {'user': current_user})

def logout_view(request):
    logout(request)
    return redirect('login_url')

