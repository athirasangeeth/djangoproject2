from django.urls import path
from . import views
from.import views

urlpatterns=[
path('school',views.samplefunction),
path('login',views.loginfunction),
path('signup',views.signupfunction),

]