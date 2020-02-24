from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class GramsView(APIView):
	def get(self,request):
		data = ["this is get"]
		return Response(data)
	def post(self,request):
		data = ["this is post"]
		return Response(data)
	def put(self,request):
		data = ["this is put"]
		return Response(data)
	def delete(self,request):
		data = ["this is delete"]
		return Response(data)
	
