from django.shortcuts import render
import datetime as dt

# Create your views here.
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to My Gallery')

def photos_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)    

