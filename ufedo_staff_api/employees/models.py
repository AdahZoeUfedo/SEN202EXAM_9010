
from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class Manager(models.Model):
    department= models.CharField(max_length=10)
    company_card = models.BooleanField(default=True)

    def str(self):
        return f"{self.department}, {self.company_card}"
    
    def get_role(self):
        return f"manager"
    
class Intern(models.Model):
    mentor=models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name="interns")
    internship_end_date = models.DateField()
    
    def str(self):
        return f"{self.mentor}, {self.internship_end_date}"

    def get_role(self):
        return f"intern"
  
class StaffBase(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def str(self):
        return f"{self.first_name} {self.last_name}"

