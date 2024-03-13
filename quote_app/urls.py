from django.urls import path
from quote_app.views import GenericQuoteView

urlpatterns = [
    path('holybook/', GenericQuoteView.as_view(), name="holybook")
]