from django.http import HttpResponse
from django.shortcuts import redirect, render
from webapp.models import ContactModel
from adminApp.models import SliderModel,ServiceModel,AboutusModel,WhyChooseModel,TeamMambersModel,NewsFromModel,LogisticsModel,AdminModel
# Create your views here.
def home(req):
    slides = SliderModel.objects.all()
    slider_info = SliderModel.objects.all()
    services = ServiceModel.objects.all()
    about_us = AboutusModel.objects.get(id=1)
    choose_info = WhyChooseModel.objects.get(id=1)
    team_info = TeamMambersModel.objects.get(id=1)
    news_info = NewsFromModel.objects.get(id=1)
    logistic_info = LogisticsModel.objects.get(id=1)
    pass_info = AdminModel.objects.get(id=1)
    obj = {"slides":slides, "services":services, "about_us":about_us, "choose_info":choose_info, "team_info":team_info, "news_info":news_info, "logistic_info":logistic_info, "slider_info":slider_info, "pass_info":pass_info}
    return render(req,"user/home.html",obj)
    
def about(req):
    about_us = AboutusModel.objects.get(id=1)
    obj = {"about_us":about_us}
    return render(req,"user/about.html",obj)

def services(req):
    return render(req,"user/services.html")

def blog(req):
    return render(req,"user/blog.html")

def contact(req):
    contact_info = ContactModel.objects.all()
    obj = {"contact_info":contact_info}
    return render(req,"user/contact.html",obj)

def save_contact(req):
    print(req.POST)
    newcontact = ContactModel(
        contact_feedback = req.POST['contact_feedback'],
        contact_name = req.POST['contact_name'],
        contact_email = req.POST['contact_email'],
        contact_subject = req.POST['contact_subject']
    )
    newcontact.save()
    # return redirect("/admin/slider")
    return redirect("/contact")