from django.contrib.auth.models import AbstractStaff
from django.db import models

# Create your models here.
class Manager(models.Model):
    department= models.CharField(max_length=10)
    company_card = models.BooleanField(default=True)

    def str(self):
        return f"{self.department}, {self.company_card}"
    
class Intern(models.Model):
    mentor=models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name="interns")
    internship_end_date = models.DateField()
    
    def str(self):
        return f"{self.mentor}, {self.internship_end_date}"


  
class StaffBase(AbstractStaff):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    company_profile = models.ForeignKey(Company_profile, on_delete=models.CASCADE, null=True, blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE)

    def str(self):
        return f"{self.first_name} {self.last_name}"
