from django.conf.urls import url
from app import views
urlpatterns = [
    url(r'^about/$',views.startView.as_view(),name='start'),
]
