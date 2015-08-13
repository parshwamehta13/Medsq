from django.db import models

# Create your models here.

class Company(models.Model):
	name = models.CharField(max_length=30,default='DEFAULT VALUE')
	job_title = models.CharField(max_length=30,default='DEFAULT VALUE')
	comapany_profile = models.CharField(max_length=200,default='DEFAULT VALUE')
	job_profile = models.CharField(max_length=200,default='DEFAULT VALUE')
	job_requirements = models.CharField(max_length=200,default='DEFAULT VALUE')
	location = models.CharField(max_length=60,default='DEFAULT VALUE')
	vacancies = models.IntegerField(default=0)
	salary = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.name