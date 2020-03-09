from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import CyberStories
from second_app.models import NCRPComplaints
from . import forms
# Create your views here.

def index(request):
    return render(request,'index.html')

def digest(request):
    return render(request, 'digest.xml')

def dict(request):
    people = {'a': {'name': 'John', 'age': '27', 'sex': 'Male'},
          'b': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
    return render(request, 'dict.html', context=people['a'])

def cyberdigest(request):
    cyber_digest_list = CyberStories.objects.order_by('Title')
    cyber_dict = {'access_records':cyber_digest_list}
    return render(request,'cyberdigest.html',context=cyber_dict)

def testingtemplate(request):
    cyber_digest_list = CyberStories.objects.order_by('-Published')
    cyber_dict = {'access_records':cyber_digest_list}
    return render(request,'testingtemplate.html',context=cyber_dict)

def ncrpdetails(request):
    ncrp_details_list = NCRPComplaints.objects.order_by('NCRPNumber')
    ncrp_details = {'access_records':ncrp_details_list}
    return render(request,'ncrpdetails.html',context=ncrp_details)

def fromscratch(request):
    form = forms.FormName()
    cyber_digest_list = CyberStories.objects.order_by('-Published')
    cyber_dict = {'access_records':cyber_digest_list}
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success")
            print(form.cleaned_data['text'])

    return render(request,'fromscratch.html',context=cyber_dict)

def previewstories(request):
    return render(request,'previewstories.html')
