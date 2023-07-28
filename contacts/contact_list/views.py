from django.shortcuts import render
from .models import Contact
from django.http import JsonResponse
# Create your views here.

def home(request):
    contacts=Contact.objects.values()
    # contact_list=list(contacts)
    return render(request,'home.html')
    # return JsonResponse(contact_list,safe=False)


def data(request):
    contacts=Contact.objects.values()
    contact_list=list(contacts)
    print(contact_list)
    return JsonResponse(contact_list,safe=False)

