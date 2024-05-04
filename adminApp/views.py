from django.http import HttpResponse
from django.shortcuts import redirect, render
from webapp.models import ContactModel
from adminApp.models import SliderModel,ServiceModel,AboutusModel,AdminModel,WhyChooseModel,TeamMambersModel,NewsFromModel,LogisticsModel
import smtplib
from email.message import EmailMessage

# EmailAdd = "omkarbhavsar50@gmail.com" #senders Gmail id over here
# Pass = "inmg tkez arov vpjl" #senders Gmail's Password over here 

# Create your views here.
def home(req):
    # msg = EmailMessage()
    # msg['Subject'] = 'Subject of the Email' # Subject of Email
    # msg['From'] = EmailAdd
    # msg['To'] = 'themadhindu007@gmail.com' # Reciver of the Mail
    # msg.set_content('Mail Omkar Body') # Email body or Content

    # #### >> Code from here will send the message << ####
    # with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: #Added Gmails SMTP Server
    #     smtp.login(EmailAdd,Pass) #This command Login SMTP Library using your GMAIL
    #     smtp.send_message(msg) #This Sends the message

    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    
    return render(req,"admin/home.html")
    
def slider(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    slides = SliderModel.objects.all()
    obj = {"slides":slides}
    return render(req,"admin/slider.html",obj)

def save_slider(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    print(req.POST)
    newslide = SliderModel(
        slider_image = req.FILES['slider_image'],
        slider_title = req.POST['slider_title'],
        slider_heading = req.POST['slider_heading'],
        slider_button_heading = req.POST['slider_button_heading'],
        slider_button_link = req.POST['slider_button_link']
    )
    newslide.save()
    return redirect("/admin/slider")

def delete_slider(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    SliderModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/slider")

def services(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    return render(req,"admin/services.html")

def save_service(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    newservice = ServiceModel(
        service_image = req.FILES['service_image'],
        service_title = req.POST['service_title'],
        service_details = req.POST['service_details']
    )
    newservice.save()
    return redirect("/admin/services")

def about_us(req):
    about_info = AboutusModel.objects.get(id = 1)
    obj = {"about_info":about_info}
    return render(req,"admin/about_us.html",obj)

def save_about_us(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    # newinfo = AboutusModel(
    #     heading = req.POST['heading'],
    #     image1 = req.FILES['image1'],
    #     image2 = req.FILES['image2'],
    #     details = req.POST['details']
    # )
    # newinfo.save()
    about_us = AboutusModel.objects.get(id=1)
    about_us.heading = req.POST['heading']
    about_us.details = req.POST['details']
    if "image1" in req.FILES:
        about_us.image1 = req.FILES['image1']
    if "image2" in req.FILES:
        about_us.image2 = req.FILES['image2']
    about_us.save()
    return redirect("/admin/about_us")

def login(req):
    return render(req,"admin/login.html")

def logout(req):
    del req.session['admin_id']
    return redirect("/admin/login")

def do_login(req):
    data = AdminModel.objects.filter(
        admin_email = req.POST['admin_email'],
        admin_password = req.POST['admin_password']
    )
    if (len(data) > 0):
        req.session['admin_id'] = data[0].id
        return redirect("/admin/")
    else:
        return redirect("/admin/login")
    
def profile(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    return render(req,"admin/profile.html")

def change_password(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    pass_info = AdminModel.objects.get(id = 1)
    obj = {"pass_info":pass_info}
    return render(req,"admin/change_password.html",obj)

def save_password(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    # pass_info = AdminModel(
    #     admin_name = req.POST['admin_name'],
    #     admin_mobile = req.POST['admin_mobile'],
    #     admin_email = req.POST['admin_email'],
    #     admin_password = req.POST['admin_password']
    # )
    # pass_info.save()
    pass_info = AdminModel.objects.get(id=1)
    pass_info.admin_name = req.POST['admin_name']
    pass_info.admin_mobile = req.POST['admin_mobile']
    pass_info.admin_email = req.POST['admin_email']
    pass_info.admin_password = req.POST['admin_password']
    pass_info.save()
    return redirect("/admin/profile")

def contact(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    contact_info = ContactModel.objects.all()
    obj = {"contact_info":contact_info}
    return render(req,"admin/contact.html",obj)

def del_contact_feedback(req):
    ContactModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/contact")

def whychoose(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    choose_info = WhyChooseModel.objects.get(id = 1)
    obj = {"choose_info":choose_info}
    return render(req,"admin/whychoose.html",obj)

def save_whychoose(req):
    print(req.POST)
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    # newchoose = WhyChooseModel(
    #     why_choose_image = req.FILES['why_choose_image'],
    #     why_choose_title = req.POST['why_choose_title'],
    #     why_choose_details = req.POST['why_choose_details'],
    #     why_choose_since = req.POST['why_choose_since'],
    #     why_choose_selector1 = req.POST['"why_choose_selector1"'],
    #     why_choose_selector2 = req.POST['why_choose_selector2'],
    #     why_choose_selector3 = req.POST['why_choose_selector3'],
    #     why_choose_selector4 = req.POST['why_choose_selector4']
    # )
    # newchoose.save()
    whychoose = WhyChooseModel.objects.get(id=1)
    whychoose.why_choose_title = req.POST['why_choose_title']
    whychoose.why_choose_details = req.POST['why_choose_details']
    whychoose.why_choose_since = req.POST['why_choose_since']
    whychoose.why_choose_selector1 = req.POST['why_choose_selector1']
    whychoose.why_choose_selector2 = req.POST['why_choose_selector2']
    whychoose.why_choose_selector3 = req.POST['why_choose_selector3']
    whychoose.why_choose_selector4 = req.POST['why_choose_selector4']
    if "why_choose_image" in req.FILES:
        whychoose.why_choose_image = req.FILES['why_choose_image']
    whychoose.save()
    return redirect("/admin/whychoose")

def teammambers(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    team_info = TeamMambersModel.objects.get(id = 1)
    obj = {"team_info":team_info}
    return render(req,"admin/teammambers.html",obj)

def save_teammambers(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    # print(req.POST)
    # teammambers = TeamMambersModel(
    # teammambers_heading = req.POST['teammambers_heading'],
    # teammambers_image1 = req.FILES['teammambers_image1'],
    # teammambers_image2 = req.FILES['teammambers_image2'],
    # teammambers_image3 = req.FILES['teammambers_image3'],
    # teammambers_image4 = req.FILES['teammambers_image4'],
    # teammambers_name1 = req.POST['teammambers_name1'],
    # teammambers_name2 = req.POST['teammambers_name2'],
    # teammambers_name3 = req.POST['teammambers_name3'],
    # teammambers_name4 = req.POST['teammambers_name4'],
    # teammambers_details1 = req.POST['teammambers_details1'],
    # teammambers_details2 = req.POST['teammambers_details2'],
    # teammambers_details3 = req.POST['teammambers_details3'],
    # teammambers_details4 = req.POST['teammambers_details4']
    # )
    # teammambers.save()
    teammambers = TeamMambersModel.objects.get(id=1)
    teammambers.teammambers_heading = req.POST['teammambers_heading']
    teammambers.teammambers_name1 = req.POST['teammambers_name1']
    teammambers.teammambers_name2 = req.POST['teammambers_name2']
    teammambers.teammambers_name3 = req.POST['teammambers_name3']
    teammambers.teammambers_name4 = req.POST['teammambers_name4']
    teammambers.teammambers_details1 = req.POST['teammambers_details1']
    teammambers.teammambers_details2 = req.POST['teammambers_details2']
    teammambers.teammambers_details3 = req.POST['teammambers_details3']
    teammambers.teammambers_details4 = req.POST['teammambers_details4']
    if "teammambers_image1" in req.FILES:
        teammambers.teammambers_image1 = req.FILES['teammambers_image1']
    if "teammambers_image2" in req.FILES:
        teammambers.teammambers_image2 = req.FILES['teammambers_image2']
    if "teammambers_image3" in req.FILES:
        teammambers.teammambers_image3 = req.FILES['teammambers_image3']
    if "teammambers_image4" in req.FILES:
        teammambers.teammambers_image4 = req.FILES['teammambers_image4']
    teammambers.save()
    return redirect("/admin/teammambers")

def edit_slider(req):
    # data = SliderModel.objects.get(id = req.GET['id'])
    # obj = {"slider_info":data}
    slider_info = SliderModel.objects.get(id = 1)
    obj = {"slider_info":slider_info}
    return HttpResponse("admin/slider",obj)

def update_slider(req):
    data = SliderModel.objects.get(id = req.POST['id'])
    data.slider_image = req.FILES['slider_image'],
    data.slider_title = req.POST['slider_title'],
    data.slider_heading = req.POST['slider_heading'],
    data.slider_button_heading = req.POST['slider_button_heading'],
    data.slider_button_link = req.POST['slider_button_link']
    data.save()
    return HttpResponse("Data Received In Post")
    # return HttpResponse("admin/slider")

def news_from(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    news_info = NewsFromModel.objects.get(id = 1)
    obj = {"news_info":news_info}
    return render(req,"admin/news_from.html",obj)

def save_news_from(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    print(req.POST)
    # news_from = NewsFromModel(
    # news_from_heading = req.POST['news_from_heading'],
    # news_from_image1 = req.FILES['news_from_image1'],
    # news_from_image2 = req.FILES['news_from_image2'],
    # news_from_details1 = req.POST['news_from_details1'],
    # news_from_details2 = req.POST['news_from_details2'],
    # news_from_date1 = req.POST['news_from_date1'],
    # news_from_date2 = req.POST['news_from_date2'],
    # news_from_steve1 = req.POST['news_from_steve1'],
    # news_from_steve2 = req.POST['news_from_steve2']
    # )
    # news_from.save()
    newsdata = NewsFromModel.objects.get(id=1)
    newsdata.news_from_heading = req.POST['news_from_heading']
    newsdata.news_from_details1 = req.POST['news_from_details1']
    newsdata.news_from_details2 = req.POST['news_from_details2']
    newsdata.news_from_date1 = req.POST['news_from_date1']
    newsdata.news_from_date2 = req.POST['news_from_date2']
    newsdata.news_from_steve1 = req.POST['news_from_steve1']
    newsdata.news_from_steve2 = req.POST['news_from_steve2']
    if "news_from_image1" in req.FILES:
        newsdata.news_from_image1 = req.FILES['news_from_image1']
    if "news_from_image2" in req.FILES:
        newsdata.news_from_image2 = req.FILES['news_from_image2']
    newsdata.save()
    return redirect("/admin/news_from")

def logistics(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    logistic_info = LogisticsModel.objects.get(id = 1)
    obj = {"logistic_info":logistic_info}
    return render(req,"admin/logistics.html",obj)

def save_logistics(req):
    if "admin_id" not in req.session:
        return HttpResponse("invalid User")
    # news_from = LogisticsModel(
    # logistics_image1 = req.FILES['logistics_image1'],
    # logistics_image2 = req.FILES['logistics_image2'],
    # logistics_heading1 = req.POST['logistics_heading1'],
    # logistics_heading2 = req.POST['logistics_heading2'],
    # logistics_name1 = req.POST['logistics_name1'],
    # logistics_name2 = req.POST['logistics_name2'],
    # logistics_founder1 = req.POST['logistics_founder1'],
    # logistics_founder2 = req.POST['logistics_founder2']
    # )
    # news_from.save()
    newdata = LogisticsModel.objects.get(id=1)
    newdata.logistics_heading1 = req.POST['logistics_heading1']
    newdata.logistics_heading2 = req.POST['logistics_heading2']
    newdata.logistics_name1 = req.POST['logistics_name1']
    newdata.logistics_name2 = req.POST['logistics_name2']
    newdata.logistics_founder1 = req.POST['logistics_founder1']
    newdata.logistics_founder2 = req.POST['logistics_founder2']
    if "logistics_image1" in req.FILES:
        newdata.logistics_image1 = req.FILES['logistics_image1']
    if "logistics_image2" in req.FILES:
        newdata.logistics_image2 = req.FILES['logistics_image2']
    newdata.save()
    return redirect("/admin/logistics")