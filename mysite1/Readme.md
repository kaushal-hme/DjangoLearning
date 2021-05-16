# Learning from django getting started part 3 

1- adding app name in urls to differentiate same name different urls present in different app.

2- using render present in django.shortcuts to simplify the template loading.

# loading template using loader present in django.
template. 
context = {
    'latest_question_list': latest_queston_list
}
template = loader.get_template('polls/index.html')
return HttpResponse(template.render(context, request))

# loading template using render present in django.shortcuts
 
context = {
        'latest_question_list': latest_queston_list
    }
return render(request, 'polls/index.html', context)

3- we can use get_object_or_404 for either getting or raising an exception. Instead of automaticaly caching.
example - 

# without using get_object_or_404
 try:
     question = Question.objects.get(pk=question_id)
 except Question.DoesNotExist:
     raise Http404("Question does not exist")
 return render(request, 'polls/details.html', {'question': question})

# with using get_object_or_404
question = get_object_or_404(Question, pk=question_id)
return render(request, 'polls/detail.html', {'question': question})
