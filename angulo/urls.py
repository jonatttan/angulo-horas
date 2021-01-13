from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('rest/clock/', views.AnguloList.as_view()),
    path('rest/clock/<int:h>/', views.AngleCalcHour.as_view()),
    path('rest/clock/<int:h>/<int:m>/', views.AnguloCalcHourMinute.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)