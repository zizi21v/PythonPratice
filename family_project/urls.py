from unicodedata import name
from django.contrib import admin
from django.urls import path
from family_app.views import create_info, list_Family
from family_project.views import family

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Family/', family, name='Family_view'),
    path('familyInfo/', create_info, name='FamilyInfo'),
    path('familyMembers/', list_Family, name='list_family')
]
