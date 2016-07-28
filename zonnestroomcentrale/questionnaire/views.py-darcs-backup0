from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext, loader
from zonnestroomcentrale.questionnaire.models import Questionnaire, QuestionnaireForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth

def index(request):
	if request.user.is_authenticated():
		try:
			questionnaire=request.user.questionnaire
		except Questionnaire.DoesNotExist:
			questionnaire=Questionnaire(user=request.user)
		if request.method == "POST":
			form = QuestionnaireForm(request.POST, instance=questionnaire)
			if form.is_valid():
				q=form.save()
				return HttpResponseRedirect('/questionnaire/thanks/')
		else:
			form= QuestionnaireForm(instance=questionnaire)
		return render_to_response('questionnaire/index.html', {"form": form, 'section':"questionnaire"}, context_instance=RequestContext(request))
	else:
		return render_to_response('questionnaire/not_logged_in.html', context_instance=RequestContext(request))
