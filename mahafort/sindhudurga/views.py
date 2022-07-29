from django.shortcuts import redirect, render
from django.views.generic import TemplateView # Import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password

from .MyClass import MyClass
from .form import InputForm

import json
# Create your views here.


# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactUsPageView(TemplateView):
    template_name = "contactus.html"
    
class DataPageView(TemplateView):
    def get(self, request, **kwargs):
        # we will pass this context object into the
        # template so that we can access the data
        # list in the template
        context = {
            'data': [
                {
                    'name': 'Celeb 1',
                    'worth': '3567892'
                },
                {
                    'name': 'Celeb 2',
                    'worth': '23000000'
                },
                {
                    'name': 'Celeb 3',
                    'worth': '1000007'
                },
                {
                    'name': 'Celeb 4',
                    'worth': '456789'
                },
                {
                    'name': 'Celeb 5',
                    'worth': '7890000'
                },
                {
                    'name': 'Celeb 6',
                    'worth': '12000456'
                },
                {
                    'name': 'Celeb 7',
                    'worth': '896000'
                },
                {
                    'name': 'Celeb 8',
                    'worth': '670000'
                }
            ]
        }

        return render(request, 'data.html', context)
    
def PlainText(request):
    return HttpResponse("return this string")
    
def FormView(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            bare_pass = cd['password']
            hashed_pass = make_password(bare_pass)#PBKDF2
            
            #check = check_password(bare_pass,hashed_pass)
            #print("password",check)

            pc = MyClass(
                first_name = cd['first_name'],
                last_name = cd['last_name'],
                roll_number = cd['roll_number'],
                password = hashed_pass
            )
            pc.save()
            return redirect("form")
        
        #return HttpResponse(json.dumps(request.POST))
    else:
        context ={}
        context['form']= InputForm()
        return render(request, "form.html", context)
