from rest_framework import viewsets
from .models import Manager, Intern, StaffBase
from .serializers import ManagerSerializer, InternSerializer, StaffBaseSerializer

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class InternViewSet(viewsets.ModelViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

class StaffBaseViewSet(viewsets.ModelViewSet):
    queryset = StaffBase.objects.all()
    serializer_class = StaffBaseSerializer

def get_role(self, manager, intern, StaffBase):
        return f"manager", "intern", "StaffBase"
        

