# from django.http import Http404
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
# from django.views.generic import TemplateView

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Returns the last five published questions
        (not including those set to be published in the future.)"""

        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        # return Question.objects.order_by('-pub_date')[:5] 

# def index(request):
#     """give view for the http request."""
    
#     latest_question_list=Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # template = loader.get_template('templates/polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))
    # return HttpResponse(output)
    # return HttpResponse("Hello, World. You're at polls index.")


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """Exclude all question that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())


# def detail(request, question_id):
#     """docstring"""
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question Does Not Exist.")

    # question = get_object_or_404(Question, pk=question_id)
    
    # return render(request, 'polls/detail.html', {'question':question})
    # return HttpResponse("You're looking at question %s."% question_id)


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def results(request, question_id):
#     """docstring"""
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request=request, template_name='polls/results.html', context={'question': question})

    # response = "You're looging for the result of question %s."
    # return HttpResponse(response % question_id)

def vote(request, question_id):
    """docstring"""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        context = {
            'question': question,
            'error_message': "You didn't select a Choice."
        }
        return render(request, 'polls/detail.html', context=context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successful dealing with POST data.
        # This prevents data from posted twice if a user hits the back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    return HttpResponse("You've voting on question %s."%question_id)
