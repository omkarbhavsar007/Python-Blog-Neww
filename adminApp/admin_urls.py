from django.contrib import admin
from django.urls import path
from adminApp import views
urlpatterns = [
    path('', views.home),
    path('slider/', views.slider),
    path('save_slider/', views.save_slider),
    path('delete_slider/', views.delete_slider),
    path('services/', views.services),
    path('save_service/', views.save_service),
    path('about_us/', views.about_us),
    path('save_about_us/', views.save_about_us),
    path('login/', views.login),
    path('do_login/', views.do_login),
    path('logout/', views.logout),
    path('profile/', views.profile),
    path('change_password/', views.change_password),
    path('save_password/', views.save_password),
    path('whychoose/', views.whychoose),
    path('save_whychoose/', views.save_whychoose),
    path('teammambers/', views.teammambers),
    path('save_teammambers/', views.save_teammambers),
    path('news_from/', views.news_from),
    path('save_news_from/', views.save_news_from),
    path('logistics/', views.logistics),
    path('update_slider/', views.update_slider),
    path('edit_slider/', views.edit_slider),
    path('save_logistics/', views.save_logistics),
    path('contact/', views.contact),
    path('del_contact_feedback/', views.del_contact_feedback)
]
