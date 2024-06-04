from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice


# VIEWS
# Poll view
def index(request):
    """ Used in urls.py to show poll.html upon empty url path.
        Handles Http requests & renders poll.html in response.
    :param request: HttpRequest
    :type request: Any
    :return: Rendered view of poll.html
    :rtype: HttpResponse
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "poll.html", context)


# Detail view
def detail(request, question_id):
    """ Used in urls.py to show detail.html upon '<int:question_id>' url path.
        Handles Http requests & renders question specific detail.html in response.
    :param request: HttpRequest
    :type request: Any
    :param question_id: Number associated with question selected in polls.html
    :type question_id: Any
    :return: Rendered view of detail.html for question selected.
    :rtype: HttpResponse
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


# Detail voting view
def vote(request, question_id):
    """ Used in urls.py to vote upon '<int:question_id>/vote/' url path.
        Handles Http requests & redirects to question specific results in response.
        Results are incremented upon voting.
    :param request: HttpRequest
    :type request: Any
    :param question_id: Number associated with question selected in polls.html
    :type question_id: Any
    :return: Redirects to results if choice is selected.
    :rtype: HttpResponse
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
        pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    # Always return an HttpResponseRedirect after successfully
    # dealing with POST data. This prevents data from being
    # posted twice if a user hits the Back button.
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
        )


# Results view
def results(request, question_id):
    """ Used in urls.py to show results.html upon 'results/' url path.
        Handles Http requests & renders question specific results in response.
    :param request: HttpRequest
    :type request: Any
    :param question_id: Number associated with question selected in polls.html
    :type question_id: Any
    :return: Renders results.html
    :rtype: HttpResponse
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})
