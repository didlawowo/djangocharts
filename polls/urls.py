from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [

    path('', login_required(views.index), name='index'),
    path('<int:question_id>/results/', login_required(views.results), name='results'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('resultsdata/<str:obj>/', views.resultsData, name="resultsdata"),
]