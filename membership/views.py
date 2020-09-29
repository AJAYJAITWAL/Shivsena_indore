from django.views import generic
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import member_form
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, "list.html", {'sks': info.objects.all(), })

class SenaCreate(CreateView):  
    model = info  
    fields = '__all__'
    template_name = 'creation_form.html'
    success_url = "/sena/{id}"

@login_required
def detail_view(request, id):
    return render(request, "sena_detail.html", {'data': info.objects.get(id=id) })
