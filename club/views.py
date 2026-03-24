from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Club
from django.db.models import Q

def club(request):
    myclubs = Club.objects.all().values()
    template = loader.get_template('all_clubs.html')
    context = {
        'myclubs': myclubs,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    myclub = Club.objects.get(id=id)
    template = loader.get_template('club_details.html')
    context = {
        'myclub': myclub,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

def template(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render())
