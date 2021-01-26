from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.template import loader, RequestContext
from django.http import HttpResponse
from django import template
from app import models
from django.db import connection
from django.contrib import messages
from .models import Customer


def index(request):
    customer = Customer.objects.order_by('out_standing')
    context = {'customer': customer}
    return render(request, 'app/index.html', context)
