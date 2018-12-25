from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def dict(request):
	response ={
	'1': 'apple',
	'2': 'ball',
	'3': 'box'
	}
	return JsonResponse(response)

def myList(request):

	myList=[ 'mariam', 'one', 'two', 3, 9, 'ok']

	return JsonResponse(myList, safe= False)