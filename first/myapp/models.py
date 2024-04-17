from django.db import models

# Create your models here.


class EmployeeModel(models.Model):
    EmployeeName=models.CharField(max_length=100,null=True,blank=True)
    EmployeeEmail=models.EmailField(max_length=100,null=True,blank=True,unique=True)
    EmployeePanNumber=models.CharField(max_length=100,null=True,blank=True)
    EmployeeMobileNumber=models.IntegerField(null=True,blank=True)
    EmployeeSalary=models.IntegerField(null=True)

