from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader
from .models import Question, Choice
from django.urls import reverse

##########################################################################################
# HELPER FUNCTIONS
##########################################################################################
def get_all_question(request):
    questions = Question.objects.all()
    response = [
        {
            'questionText': question['question_text'],
            'pubDate': uqestion['pub_date']
        }
        for question in questions
    ]
    return JsonResponse({'questions': response})


def create_question():
    pass


##########################################################################################
# MAIN FUNCTIONS
##########################################################################################
def index(request):
    if request.method == 'GET':
        return get_all_question(request)
    if request.method == 'POST':
        return create_question(request)


def detail(request, question_id):
    try:
        question = Question.objects.filter(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return JsonResponse(
        {
            'questionText': question['question_text'],
            'pubDate': uqestion['pub_date']
        }
    )


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def create_question():
    pass
