from django.urls import path


from .views import AutoList, AutoDetailList, CreateAuto, CreateAutoBrand, CreateAutoModel


urlpatterns = [
    path('', AutoList.as_view(), name='auto_list'),
    path('auto_list/', AutoList.as_view(), name='auto_list'),
    path('auto_list/<int:pk>', AutoDetailList.as_view(), name='auto_vin'),
    path('auto_create/', CreateAuto.as_view(), name='auto_create'),

    path('create_auto_brand/', CreateAutoBrand.as_view(), name='auto_update'),
    path('create_auto_model/', CreateAutoModel.as_view(), name='auto_update'),
    ]
#-----------------------------------------------------




