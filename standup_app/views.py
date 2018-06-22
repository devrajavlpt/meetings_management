# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import UserProfile,Employee,Salary
from .Serializer import UserSerializer,EmployeeSerializer,SalarySerializer

class UserListView(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	permission_classes = (AllowAny,)

	def get_queryset(self):
		queryset = UserProfile.objects.all()
		username = self.request.query_params.get('username')
		print username,type(username)
		if username:
			queryset = queryset.filter(username=str(username))
			print queryset
		return queryset

class EmployeeView(viewsets.ModelViewSet):
	serializer_class = EmployeeSerializer
	permission_classes = (AllowAny,)
	def get_queryset(self):
		queryset = Employee.objects.all()

class SalaryView(viewsets.ModelViewSet):
	serializer_class = SalarySerializer
	permission_classes = (AllowAny,)
	def get_queryset(self):
		queryset = Salary.objects.all()