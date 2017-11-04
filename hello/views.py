from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

views = Blueprint('views', __name__)

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

@app.route("/")
def index():
    if request.method == "POST":
    	render_template("index.html", result = "This FUCKING WORKED!!")
    else:
    	render_template("index.html", result = "we fucked up!!!")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

