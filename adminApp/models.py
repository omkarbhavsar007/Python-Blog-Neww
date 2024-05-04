from django.db import models

# Create your models here.
class SliderModel(models.Model):
        slider_image = models.ImageField(upload_to="static/uploads/")
        slider_title = models.CharField(max_length = 200)
        slider_heading = models.CharField(max_length = 200)
        slider_button_heading = models.CharField(max_length = 200)
        slider_button_link = models.CharField(max_length = 200)

class ServiceModel(models.Model):
        service_image = models.ImageField(upload_to="static/uploads/")
        service_title = models.CharField(max_length = 200)
        service_details = models.TextField()

class AboutusModel(models.Model):
        heading = models.CharField(max_length = 200)
        details = models.TextField()
        image1 = models.ImageField(upload_to="static/uploads/")
        image2 = models.ImageField(upload_to="static/uploads/")

class AdminModel(models.Model):
        admin_name = models.CharField(max_length = 100)
        admin_mobile = models.CharField(max_length = 15)
        admin_email = models.CharField(max_length = 200)
        admin_password = models.CharField(max_length = 100)

class WhyChooseModel(models.Model):
        why_choose_image = models.ImageField(upload_to="static/uploads/")
        why_choose_title = models.CharField(max_length = 200)
        why_choose_details = models.TextField()
        why_choose_since = models.TextField()
        why_choose_selector1 = models.CharField(max_length = 200)
        why_choose_selector2 = models.CharField(max_length = 200)
        why_choose_selector3 = models.CharField(max_length = 200)
        why_choose_selector4 = models.CharField(max_length = 200)
        
class TeamMambersModel(models.Model):
        teammambers_heading = models.CharField(max_length = 200)
        teammambers_image1 = models.ImageField(upload_to="static/uploads/")
        teammambers_image2 = models.ImageField(upload_to="static/uploads/")
        teammambers_image3 = models.ImageField(upload_to="static/uploads/")
        teammambers_image4 = models.ImageField(upload_to="static/uploads/")
        teammambers_name1 = models.CharField(max_length = 100)
        teammambers_name2 = models.CharField(max_length = 100)
        teammambers_name3 = models.CharField(max_length = 100)
        teammambers_name4 = models.CharField(max_length = 100)
        teammambers_details1 = models.CharField(max_length = 100)
        teammambers_details2 = models.CharField(max_length = 100)
        teammambers_details3 = models.CharField(max_length = 100)
        teammambers_details4 = models.CharField(max_length = 100)

class NewsFromModel(models.Model):
        news_from_heading = models.CharField(max_length = 200)
        news_from_image1 = models.ImageField(upload_to="static/uploads/")
        news_from_image2 = models.ImageField(upload_to="static/uploads/")
        news_from_date1 = models.CharField(max_length = 100)
        news_from_date2 = models.CharField(max_length = 100)
        news_from_details1 = models.TextField()
        news_from_details2 = models.TextField()
        news_from_steve1 = models.CharField(max_length = 100)
        news_from_steve2 = models.CharField(max_length = 100)
        
class LogisticsModel(models.Model):
        logistics_heading1 = models.CharField(max_length = 200)
        logistics_heading2 = models.CharField(max_length = 200)
        logistics_image1 = models.ImageField(upload_to="static/uploads/")
        logistics_image2 = models.ImageField(upload_to="static/uploads/")
        logistics_name1 = models.CharField(max_length = 100)
        logistics_name2 = models.CharField(max_length = 100)
        logistics_founder1 = models.TextField()
        logistics_founder2 = models.TextField()
