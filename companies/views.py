from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse
from companies.models import Company

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the companies index.")

def index1(request):
    return HttpResponse("Hello, world. You're at the companies index1.")

def detail(request, company_id):
    return HttpResponse("You're looking at company %s." % company_id)

def result(request, company_id):
    response = "You're looking at the results of company %s."
    return HttpResponse(response % company_id)

def applied(request, company_id):
    return HttpResponse("You're applying on company %s." % company_id)

def listCompanies(request):
	# if 'q' in request.GET and request.GET['q']:
	# 	q = request.GET['q']
	# 	companyList = Company.objects.filter(name__icontains=q)
	# else:
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
		html = t.render(Context({'company_list':newList,'location_list':location_list}))
		return HttpResponse(html)
	else:
		t = get_template('database.html')
		html = t.render(Context({'location_list':location_list,'company_list':companyList}))
		return HttpResponse(html)		

def companyProfile(request,company_id):
	companyObject = Company.objects.filter(id=company_id)
	t = get_template('companyProfile.html')
	html = t.render(Context({'item':companyObject[0]}))
	return HttpResponse(html)


# def search_form(request):
#     return render(request, 'search_form.html')

# def search(request):
#     if 'q' in request.GET:
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)
	