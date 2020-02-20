from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from useful.models import Members
from django.views.generic import View
# Create your views here.

class MembersView(View):
  def index(request):
    return HttpResponse(serializers.serialize('json', Members.objects.all()))

  def add(request):
    return HttpResponse(serializers.serialize('json', request))
