from django.shortcuts import render

from django.template.loader import render_to_string
from django.test import TestCase, Client
from user_contacts.models import Person, Phone
from user_contacts.views import *

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from user_contacts import new_contact_form

# Create your views here.

class ViewTest(TestCase):

    def setUp(self):
        self.client_stub = Client()

    def test_view_home_route(self):
        response = self.client_stub.get('/')
        self.assertEquals(response.status_code, 200)

    def home(request):
        return render_to_response('index.html')

    def all_contacts(request):
        contacts = Phone.objects.all()
        return render_to_response('all.html', {'contacts':contacts})

    def add(request):
        person_form = new_contact_form.ContactForm()
        #return render(request, 'add.html', {'person_form' : person_form}, context_instance = RequestContext(request))
        return render(request, 'add.html', {'person_form' : person_form})

    def create(request):
        form = new_contact_form.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('all/')
        return render(
            #request, 'add.html', {'person_form' : form}, context_instance=RequestContext(request))
            request, 'add.html', {'person_form' : form})
