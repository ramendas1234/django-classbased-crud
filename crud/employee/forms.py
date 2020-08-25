from django.forms import ModelForm
from employee.models import Employee

# Create your forms here.

class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
		fields = ('__all__')