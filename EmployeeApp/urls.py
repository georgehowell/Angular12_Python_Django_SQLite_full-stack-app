from django.conf.urls import url
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings



urlpatterns=[
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),

    url(r'^employees$',views.employeesApi),
    url(r'^employees/([0-9]+)$',views.employeesApi),

    url(r'^savefile',views.savefile)
]+static(setings.MEDIA_URL,document_root=settings.MEDIA_ROOT)