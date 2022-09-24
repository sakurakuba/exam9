from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from rest_framework import serializers


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "base.html")
