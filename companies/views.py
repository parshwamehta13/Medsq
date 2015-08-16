from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from companies.models import Company,Resume
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.

def apply(request, company_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/index')
	elif request.method == 'POST':
		company = Company.objects.filter(id=company_id)
		status = "Applied"
		name = request.POST['name_applicant']
		cv = request.POST['cv_applicant']
		recruiter = request.user.id
		temp = Resume(name_applicant=name,cv_applicant=cv,status_application=status,company_applied=company[0],recruiter_id=recruiter)
		temp.save()
		return HttpResponseRedirect('/company/')
	else:
		return render(request,'apply.html')


def listCompanies(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/index')
	elif 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		companyList = Company.objects.filter(name__icontains=q)
	else:
		companyList = Company.objects.all()
	location = []
	newList = []

	l = Company.objects.all().values('location').distinct()
	location_list = []
	for i in l:
		location_list.append(i['location'])

	for i in location_list:
		if str(i) in request.GET:
			location.append(str(i))
	if len(location)!=0:
		for i in companyList:
			if i.location in location:
				newList.append(i)
		t = get_template('database.html')
		html = t.render(Context({'company_list':newList,'location_list':location_list,'user':request.user}))
		return HttpResponse(html)
	else:
		t = get_template('database.html')
		html = t.render(Context({'location_list':location_list,'company_list':companyList,'user':request.user}))
		return HttpResponse(html)		


def companyProfile(request,company_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/index')
	companyObject = Company.objects.filter(id=company_id)
	t = get_template('companyProfile.html')
	appliedCandidates = Resume.objects.all()
	requiredCandidates = []
	for i in appliedCandidates:
		if i.company_applied.id == companyObject[0].id:
			requiredCandidates.append(i)
	html = t.render(Context({'item':companyObject[0],'applied_candidates':requiredCandidates}))
	return HttpResponse(html)


# def search_form(request):
#     return render(request, 'search_form.html')

# def search(request):
#     if 'q' in request.GET:
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)
	