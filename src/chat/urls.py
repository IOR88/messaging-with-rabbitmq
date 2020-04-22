from django.conf import urls
from chat import views
from rest_framework import routers


router = routers.DefaultRouter()
# router.register(r'^data', views.DataViewSet)

urlpatterns = [
    urls.url('^home/$', views.BaseView.as_view()),
] + router.urls
