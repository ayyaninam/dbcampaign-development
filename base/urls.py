from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("services", views.services_page, name="services_page"),
    path("service-detail-page/<str:title_str>", views.service_detail_page, name="service_detail_page"),
    path("leads-collector/<int:service_id>", views.leads_collector, name="leads_collector"),
    path("heart-btn-clicked", views.heart_btn_clicked, name="heart_btn_clicked"),
    path("newsletter-emails-collector", views.newsletter_emails_collector, name="newsletter_emails_collector"),
]
