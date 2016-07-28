from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from zonnestroomcentrale.accounts.models import Profile, ProfileForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method=='POST':
		regform = UserCreationForm(request.POST)
		if regform.is_valid():
			regform.save()
			new_user = auth.authenticate(username=request.POST['username'],password=request.POST['password1'])
			auth.login(request, new_user)
			return HttpResponseRedirect("/accounts/profile/")
	else:
		regform=UserCreationForm()
	return render_to_response('register.html',{'regform': regform, 'loginform': AuthenticationForm(), 'section': 'register', 'failure': False},RequestContext(request))
	
def login(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		# Correct password, and the user is marked "active"
		auth.login(request, user)
		# Redirect to a success page.
		return HttpResponseRedirect("/accounts/profile/")
	else:
		loginform=AuthenticationForm()
		loginform.initial={'username':username}
		# Show an error page
	return render_to_response('register.html',\
	{'regform': UserCreationForm(), 'loginform': loginform,\
	 'section': 'register', 'failure': True},RequestContext(request))

@login_required
def profile(request):
	try:
		profile=request.user.get_profile()
	except Profile.DoesNotExist:
		profile=Profile(user=request.user, keep_me_up_to_date=True)
	
	if request.method=='POST':
		new_profile=ProfileForm(request.POST, instance=profile)
		if new_profile.is_valid():
			new_profile.save()
			return HttpResponseRedirect("/questionnaire/")
	else:
		new_profile=ProfileForm(instance=profile)
	
	return render_to_response('profile.html',\
	{'profileform': new_profile, 'section':'profile'}, context_instance=RequestContext(request))
