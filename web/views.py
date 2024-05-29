from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
  return HttpResponse("인덱스입니다!! 안녕하세요, dgsgs")