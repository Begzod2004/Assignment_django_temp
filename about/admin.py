from django.contrib import admin
from .models import CompanyInfo, Facts, Employee, Service, News, Testimonial

admin.site.register(CompanyInfo)
admin.site.register(Facts)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Employee)
admin.site.register(News)
