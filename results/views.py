from django.shortcuts import render

from polls.models import Question




def all_results(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'results/index.html', context)