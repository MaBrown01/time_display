from django.shortcuts import render
import datetime


# Create your views here.
def index(request):
        current = {
            "time":datetime.datetime.now()

        }

        return render (request, 'main/index.html', current)
