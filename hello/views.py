from django.shortcuts import render
from django.http import HttpResponse
from flask import Flask, flash, redirect, render_template, request, session

from .models import Greeting

# app = Flask(__name__)

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

# @app.route("/")
# def index(request):
#     if request.method == "POST":
#     	render_template("index.html", result = "This FUCKING WORKED!!")
#     else:
#     	render_template("index.html", result = "we fucked up!!!")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

