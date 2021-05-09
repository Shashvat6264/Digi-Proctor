from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Urls for Students
    path('all/', views.all_quizes, name='all_quizzes'),
    path('<int:quizID>/', views.quiz_start, name='quiz_start'),
    path('<int:quizID>/<int:questionID>/<int:responseID>/', views.displayquizqn, name='displayquizqn'),
    path('over/', views.quizOver, name='quizOver'),
    # Urls for Professors
    path('create/', views.createQuiz, name='createQuiz'),
    path('create/question/', views.createQuestion, name='createQuestion'),
    path('show/', views.showQuiz, name='showQuiz'),
    path('show/<int:quizID>/', views.showResponses, name='showResponses'),
    path('show/<int:quizID>/responses/<int:reponseQuizID>/', views.showAResponse, name='showAResponse'),
    # Urs for Login
    path('register/', views.registerView, name='registerView'),
    path('login/', LoginView.as_view(), name='login_url'), 
    path('dashboard/', views.dashboardRedirect, name='dashboardRedirect'),
    path('student', views.StudentHome, name='StudentHome'),
    path('prof/', views.ProfHome, name='ProfHome'),
    path('logout/', views.logout_view, name='logout'),
]