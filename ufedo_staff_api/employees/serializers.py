# employees/serializers.py

from rest_framework import serializers
from .models import Manager, Intern, StaffBase  # Import your models

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields=('id', 'hire_date', 'created_at', 'updated_at', 'has_company_card')
        model = Manager
        fields = '__all__'  

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields=('id', 'hire_date', 'created_at', 'updated_at', 'has_company_card')
        model = Intern
        fields = '__all__'

class StaffBaseSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields=('id', 'hire_date', 'created_at', 'updated_at', 'has_company_card')
        model = StaffBase
        fields = '__all__'
    
