from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=50)          
    location = models.CharField(max_length=50)      
    about = models.TextField(blank=True, null=True) 
    
    TYPE_CHOICES = (
        ('IT', 'IT'), 
        ('Non IT', 'Non IT'), 
        ('Mobile Phones', 'Mobile Phones'),
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICES) 
    added_date = models.DateTimeField(auto_now=True)             
    active = models.BooleanField(default=True)  
    
    def __str__(self):
        return self.name  
 
# Employee Model                  
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50, choices=(
                                ('Manager', 'manager'),
                                ('Softer developer', 'sd'),
                                ('Project Leader', 'pl')
                              ))
    company=models.ForeignKey(Company, on_delete=models.CASCADE)