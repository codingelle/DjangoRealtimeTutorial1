from django.urls import path

from .views import IndexView, PostStreamView

app_name = 'post'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('stream/', PostStreamView.as_view(), name='stream'),
]
