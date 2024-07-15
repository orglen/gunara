from django.shortcuts import render
from django.http import (
    HttpResponse,

)
import json
from Gunara.config import models
# Create your views here.

def index(request):
    return render(request,'index.html')

def get_models(request):
    return HttpResponse(json.dumps(models))
