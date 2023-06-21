
from django.urls import path
from sear import views
app_name='sear'

urlpatterns = [

    path('searchresult',views.searchresult,name="searchresult"),

]

