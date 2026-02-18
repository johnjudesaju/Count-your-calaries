from django.urls import path

from app_core import views


app_name="app_core"

urlpatterns = [
    # path("district/",views.dis_entry,name="dis_entry"),
    # path("disview",views.dis_view),
    # path("disdel/",views.dis_del),
    # path("disedit/",views.dis_upd),

    path("location/",views.loc_entry,name="loc_entry"),
    path("locview/",views.loc_view,name="loc_view"),
    path("locdel/<int:no>",views.loc_del,name="loc_del"),
    path("locupd/<int:no>",views.loc_upd,name="loc_upd"),

    path("category/",views.cat_entry,name="cat_entry"),
    path("catview/",views.cat_view,name="cat_view"),
    path("catdel/<int:no>",views.cat_del,name="cat_del"),
    path("catedit/<int:no>",views.cat_upd,name="cat_upd"),
    path("card/",views.card),

    path("ingredients/",views.ing_entry,name="ing_entry"),
    path("ing_view/",views.ing_view,name="ing_view"),
    path("ing_del/<int:no>",views.ing_del,name="ing_del"),
    path("ing_edit/<int:no>",views.ing_upd,name="ing_upd"),

    path("smoothie/",views.smoothie_entry,name="smoothie_entry"),
    path("smoothie_view/",views.smoothie_view,name="smoothie_view"),
    path("smoothie_del/<str:no>",views.smoothie_del,name="smoothie_del"),
    path("smoothie_edit/<int:no>",views.smoothie_upd,name="smoothie_upd"),

    path("customer_view/",views.c_view,name="c_view"),
    path("delivery_reg/",views.delivery_reg,name="d_reg"),
    path("delivery_view/",views.delv_view,name="d_view"),
    path("delv_acpt/<int:no>",views.delv_acpt,name="delv_acpt"),
    path("delv_rgct/<int:no>",views.delv_rgct,name="delv_rgct"),
    path("cust_smoothie/",views.cust_smoothieview,name="cust_smoothie"),
    path("custz_smoothie/",views.custz_smoothie,name="custz_smoothie"),
    path("smoothie_details/<int:no>",views.smoothie_details,name="smoothie_details"),
    path("add_fav/<int:no>",views.add_fav,name="add_fav"),
    path("fav/",views.fav,name="fav"),
    # path("payment/",views.payment,name="payment"),
]