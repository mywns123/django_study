from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("장고 훈련소에 오신것을 환영합니다.")
