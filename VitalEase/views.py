from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'title': 'VitalEase-main-page'})
def medication(request):
    return render(request, 'medication.html', {'title': 'Medication_page'})
def contact(request):
    return render(request, 'contact.html', {'title': 'Emergency_Contact'})
def caregiver(request):
    return render(request, 'caregiver.html', {'title': 'Caregiver_Page'})
