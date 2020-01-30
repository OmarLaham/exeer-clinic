from django.urls import path
from . import views

app_name = 'exeerapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('help-guide', views.HelpGuideView.as_view(), name='help_guide'),
    path('consultant-profile', views.ConsultantProfileView.as_view(), name='consultant_profile'),
    path('question/new', views.QuestionNewView.as_view(), name='question_new',),
    path('question/<int:pk>', views.QuestionView.as_view(), name='question'),
]
