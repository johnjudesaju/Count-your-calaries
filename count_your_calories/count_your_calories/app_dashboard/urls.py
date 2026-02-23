from django.urls import path

from app_dashboard import views


app_name="app_dashboard"

urlpatterns = [
    path("adm/",views.appdash),
    path("",views.index,name="index"),
    path("log/",views.log,name="log"),
    path("reg/",views.customer_reg,name="reg"),
    path("customerdash/",views.customer_dash,name="c_dash"),
    path("delv_dash/",views.delv_dash,name="delv_dash"),
    path("logout/",views.logout_view,name='logout'),

]