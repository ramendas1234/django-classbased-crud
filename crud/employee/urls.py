from django.urls import path
from employee.views import  EmployeeList,test,EmployeeCreate,EmployeeUpdate,EmployeeDelete

urlpatterns = [
    # ...
    path('employee/add/', EmployeeCreate.as_view(), name='author-add'),
    path('employee/<pk>/update/', EmployeeUpdate.as_view(), name='author-update'),
    path('employee/<pk>/delete/', EmployeeDelete.as_view(), name='author-delete'),
    path('', EmployeeList.as_view(), name='index'),
    path('thankyou/', test, name='test'),
    # path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
]