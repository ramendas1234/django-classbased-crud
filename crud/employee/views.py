from employee.models import Employee
from employee.forms import EmployeeForm
from django.views.generic import ListView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.http.response import HttpResponse

'''class EmployeeAdd(FormView):
    
    form_class = EmployeeForm
    template_name = 'add.html'
    success_url = reverse_lazy('index')
    # success_url = '/thankyou/'
    def form_valid(self, form):
        form.save()
        return super(EmployeeAdd, self).form_valid(form) '''

class EmployeeList(ListView):
	model = Employee
	template_name = 'index.html'

def test(request):
	return HttpResponse('dfgfg')

class EmployeeCreate(CreateView):
    model = Employee
    template_name = 'add.html'
    success_url = reverse_lazy('index')
    fields = ('__all__')

class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = 'update.html'
    success_url = reverse_lazy('index')
    fields = ('__all__')
class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'delete.html'
    success_url = reverse_lazy('index')
    