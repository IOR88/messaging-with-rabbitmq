from django.conf import urls
from chat import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'^messages', views.MessageViewSet)

urlpatterns = [
    urls.url('^base/$', views.BaseView.as_view()),
    urls.url('^users/active/$', views.ActiveUsers.as_view()),
] + router.urls