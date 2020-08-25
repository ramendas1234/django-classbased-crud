from django.db import models
from django.utils import timezone
# Create your models here.

DEPARTMENT_CHOICES = [('accountant','Accountant'),('hr','HR'),('marketing','Marketing'),('network','Network'),('operation_manager','Operation Manager'),('it_production','IT Production')]
class Employee(models.Model):
	
	
	name = models.CharField(max_length=100, blank=True, default='')
	dob = models.DateField(default = timezone.now, blank = True)
	email = models.CharField(default='',max_length=100)
	department = models.CharField(choices=DEPARTMENT_CHOICES, default='it_production', max_length=100)
	designation = models.CharField(default='',max_length=100)
	salary = models.CharField(default='',max_length=100)
	address = models.TextField(default='',blank = True,max_length=1000)
	def __str__(self):
		return self.name